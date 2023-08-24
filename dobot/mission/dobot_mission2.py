import rclpy as rp
import cv2
import threading

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from yolo_inference.msg import Yolov8Inference


import threading
from yolo_pkg.dobot_api import DobotApiDashboard, DobotApi, DobotApiMove, MyType
from time import sleep

import math

import numpy as np

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()

	def top(self):
		if not self.is_empty():
			return self.items[-1]

	def size(self):
		return len(self.items)

# 로봇이 이동하고자 하는 좌표 (x, y, z, yaw) unit : mm, degree
point_home0 = [245, 5, 50, 115]
point_zero = [255, 0, 0, 115]
point_grip = [304, 19, -25, 16]
point_parse = [255, -54, -5, 115]
point_home1 = [209, 0, 46, 115]
point_home = [209, 0, -40, 115]


point_yellow = [245, 110, -57, 115]
point_green = [337, 12, -57, 115]
point_red = [247, -103, -57, 116]

# First point is ArUCo marker point
points_yellow_area = [[245, 110], [290, 125], [210, 66], [210, 120]]
check_list_yellow_area = [False, False, False, False]
points_green_area = [[331, 10], [345, -53], [340, 76], [281, -16], [275, 36], [240, 6]] # Order to Pyramid
check_list_green_area = [False, False, False, False, False, False]
points_red_area = [[246,-102], [294,-107], [211,-58], [207,-105]]
check_list_red_area = [False, False, False, False]

cv_bridge = CvBridge()
img = None

class YOLOsubscriber(Node):
	def __init__(self):
		super().__init__("yolo_subscriber")

		# 입력 파라미터
		self.ip = "192.168.1.6" # Robot의 IP 주소
		self.gripper_port = 1   # 그리퍼 포트 번호
		self.speed_value = 100   # 로봇 속도 (1~100 사이의 값 입력)

		# 로봇 연결
		self.dashboard, self.move, self.feed = self.connect_robot(self.ip)
		self.dashboard.EnableRobot()
		print("이제 로봇을 사용할 수 있습니다!")


		# 쓰레드 설정
		self.feed_thread = threading.Thread(target=self.get_feed, args=(self.feed,))
		self.feed_thread.setDaemon(True)
		self.feed_thread.start()
		# 전역 변수 (현재 좌표)
		self.current_actual = None# 로봇 상태 초기화 1 : 로봇 에러 메시지 초기화
		self.robot_clear(self.dashboard)
		# 로봇 상태 초기화 2 : 로봇 속도 조절
		self.robot_speed(self.dashboard, self.speed_value)
		# 로봇 현재 위치 받아오기 (x, y, z, yaw) - 로봇 베이스 좌표계
		self.get_Pose(self.dashboard)

		self.run_point(self.move, point_home)


		self.img_sub = self.create_subscription(
			Image,
			'image_raw',
			self.camera_callback,
			10
		)

		self.yolo_sub = self.create_subscription(
			Yolov8Inference,
			'/yolov8_inference',
			self.yolo_callback,
			10
		)
		self.img = None
		self.curr_blocks = list()
		self.layer_mode = 2

	def connect_robot(self, ip):
		try:
			dashboard_p = 29999
			move_p = 30003
			feed_p = 30004
			print("연결 설정 중...")
			dashboard = DobotApiDashboard(ip, dashboard_p)
			move = DobotApiMove(ip, move_p)
			feed = DobotApi(ip, feed_p)
			print("연결 성공!!")
			return dashboard, move, feed
		except Exception as e:
			print("연결 실패")
			raise e

	def robot_clear(self, dashboard : DobotApiDashboard):
		dashboard.ClearError()
		
	def robot_speed(self, dashboard : DobotApiDashboard, speed_value):
		dashboard.SpeedFactor(speed_value)

	def gripper_DO(self, dashboard : DobotApiDashboard, index, status):
		dashboard.ToolDO(index, status)
		
	def get_Pose(self, dashboard : DobotApiDashboard):
		dashboard.GetPose()
		
	def run_point(self, move: DobotApiMove, point_list: list):
		move.MovL(point_list[0], point_list[1], point_list[2], point_list[3])
		
	def get_feed(self, feed: DobotApi):
		# current_actual
		hasRead = 0
		while True:
			data = bytes()
			while hasRead < 1440:
				temp = feed.socket_dobot.recv(1440 - hasRead)
				if len(temp) > 0:
					hasRead += len(temp)
					data += temp
			hasRead = 0
			a = np.frombuffer(data, dtype=MyType)
			if hex((a['test_value'][0])) == '0x123456789abcdef':
				self.current_actual = a["tool_vector_actual"][0] # Refresh Properties
			sleep(0.001)
			
	def wait_arrive(self, point_list):
		# current_actual
		while True:
			is_arrive = True
			if self.current_actual is not None:
				for index in range(4):
					if (abs(self.current_actual[index] - point_list[index]) > 1):
						is_arrive = False
				if is_arrive:
					return
			sleep(0.001)


	def trans_img_to_rbt(self, x_i, y_i):
		x_r = 180 + 210 / 480 * y_i
		y_r = -135 + 285 / 640 * x_i
		return (x_r, y_r)

	def shutdown(self):
		self.dashboard.DisableRobot()


	def run_phase_0_logic(self):
		x_r, y_r = self.trans_img_to_rbt(self.x_i, self.y_i)
		# print(self.x_i, self.y_i)
		print(x_r, y_r)
		# 로봇 구동 1 (point_init)
		self.run_point(self.move, [x_r, y_r, 0, 115])
		self.run_point(self.move, [x_r, y_r, -25, 115])
		# wait_arrive(point_home)
		# sleep(5)

		# 그리퍼 구동
		self.gripper_DO(self.dashboard, self.gripper_port, 1)
		# sleep(5)

		# 로봇 구동 2 (point_init)
		self.run_point(self.move, [point_red[0], point_red[1], -25, 115])
		self.run_point(self.move, point_red)
		# wait_arrive(point_home)
		# sleep(5)

		# 그리퍼 끄기
		self.gripper_DO(self.dashboard, self.gripper_port, 0)
		self.run_point(self.move, [point_red[0], point_red[1], 0, 115])
		sleep(3)

	def get_height_layer(self, layer):
		ret = 0
		if layer == 3:
			ret = -27
		elif layer == 2:
			ret = -44
		elif layer == 1:
			ret = -60
		return ret

	def get_color_pose(self, str_clr):
		print(str_clr)
		print(type(str_clr))
		ret_pose = [245, 5]
		pose_yellow = self.my_yellow_pose
		pose_green = self.my_green_pose
		pose_red = self.my_red_pose
		if pose_yellow == [0.0, 0.0]:
			pose_yellow = [245, 110]
		if pose_green == [0.0, 0.0]:
			pose_green = [337, 12]
		if pose_red == [0.0, 0.0]:
			pose_red = [247, -103]
		if str_clr == "red":
			ret_pose = pose_red
		elif str_clr == "green":
			ret_pose = pose_green
		elif str_clr == "yellow":
			ret_pose = pose_yellow
		return ret_pose

	def set_my_color_pose(self, color_name, x_cntr, y_cntr):
		x_r, y_r = self.trans_img_to_rbt(x_cntr, y_cntr)
		if (color_name == "red"):
			self.my_red_pose = [x_r, y_r]
		if (color_name == "green"):
			self.my_green_pose = [x_r, y_r]
		if (color_name == "yellow"):
			self.my_yellow_pose = [x_r, y_r]

	def is_inside_triangle(self, A, B, C, P):
		denominator = ((B[1] - C[1]) * (A[0] - C[0]) +
					   (C[0] - B[0]) * (A[1] - C[1]))
		a = ((B[1] - C[1]) * (P[0] - C[0]) +
			 (C[0] - B[0]) * (P[1] - C[1])) / denominator
		b = ((C[1] - A[1]) * (P[0] - C[0]) +
			 (A[0] - C[0]) * (P[1] - C[1])) / denominator
		c = 1 - a - b
		if a >= 0 and b >= 0 and c >= 0:
			return True
		else:
			return False

	def is_in_yellow_area(self, point):
		A = (313, 130)
		B = (200, 125)
		C = (200, 48)
		return self.is_inside_triangle(A, B, C, point)

	def is_in_green_area(self, point):
		A = (358, 106)
		B = (360,-87)
		C = (220, 4)
		return self.is_inside_triangle(A, B, C, point)

	def is_in_red_area(self, point):
		A = (207, -40)
		B = (206,-114)
		C = (315,-115)
		return self.is_inside_triangle(A, B, C, point)

	def is_conflicting_each_block_points(self, point_a, point_b):
		dist = math.sqrt( (point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2 )
		# 285.234244,66.653331
		# 279.382155,115.301753
		if dist <= 45:
			return True
		else:
			return False

	def is_block_conflicting_point(self, point):
		for each_block in self.curr_blocks:
			if self.is_conflicting_each_block_points(point, (each_block["x_center"], each_block["y_center"])) == True:
				return True
		return False

	def get_points_by_color(self, color):
		if (color == "yellow"):
			return points_yellow_area
		elif (color == "green"):
			return points_green_area
		elif (color == "red"):
			return points_red_area

	def get_check_list_by_color(self, color):
		check_list = []
		if color == "yellow":
			check_list = check_list_yellow_area
		elif color == "green":
			check_list = check_list_green_area
		elif color == "red":
			check_list = check_list_red_area
		return check_list

	def is_checked_already_posed(self, idx, color):
		check_list = []
		if color == "yellow":
			check_list = check_list_yellow_area
		elif color == "green":
			check_list = check_list_green_area
		elif color == "red":
			check_list = check_list_red_area
		return check_list[idx]

	def get_valid_point_in_proper_area(self, block):
		block_color = block["color_name"]
		# block_point = (block["x_center"], block["y_center"])

		points_of_the_area = self.get_points_by_color(block_color)

		for idx, each_color_point in enumerate(points_of_the_area):
			if self.is_block_conflicting_point(each_color_point) == False and self.is_checked_already_posed(idx, block_color) == False:
				check_list = self.get_check_list_by_color(block_color)
				check_list[idx] = True
				return each_color_point
		return (-1, -1) # not valid

	def camera_callback(self, msg):
		self.img = cv_bridge.imgmsg_to_cv2(msg, "bgr8")
		return
		if self.img is not None:
			cv2.imshow('Yolo detections', self.img)
			cv2.waitKey(1)

	def yolo_callback(self,msg):
		print("In yolo callback")
		for result in msg.yolov8_inference:

			class_name = result.label
			top = result.top
			top_left = result.top_left
			bottom = result.bottom
			bottom_right = result.bottom_right
			conf = round(result.conf, 2)
			# self.get_logger().info(f"{class_name} : {top}, {top_left}, {bottom}, {bottom_right} / {conf}")

			y_i = (top_left + bottom_right) / 2
			x_i = (top + bottom) / 2
			x_c, y_c = self.trans_img_to_rbt(x_i, y_i)
			self.curr_blocks.append({"color_name": class_name, "x_center": x_c, "y_center" : y_c})

			# print("야 보임?")
			# if self.img is not None:
			# 	cv2.rectangle(self.img, (top, top_left), (bottom, bottom_right), (255, 255, 0))
			# 	cv2.putText(self.img, f"{class_name} : {conf:.2f}", (top, top_left), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (255, 0, 255), 2)

		# if self.img is not None:
		# 	cv2.imshow('Yolo detections', self.img)
		# 	cv2.waitKey(1)

		is_all_valid = True

		if self.layer_mode == 2:
			is_all_valid = False

		for each in self.curr_blocks:
			flag_valid = False
			print("each: ")
			print(each)
			# Check each color areas
			target_point = (each["x_center"], each["y_center"])
			if self.layer_mode < 2:
				if each["color_name"] == 'yellow':
					if self.is_in_yellow_area((each["x_center"], each["y_center"])) == True:
						print("Is in yellow area!!!!!!!!!!!!!")
						flag_valid = True
					else :
						print("Get out of here and Go to yellow!!")
				elif each["color_name"] == 'green':
					if self.is_in_green_area((each["x_center"], each["y_center"])) == True:
						print("Is in green area!!!!!!!!!!!!!")
						flag_valid = True
					else :
						print("Get out of here and Go to green!!")
				elif each["color_name"] == 'red':
					if self.is_in_red_area((each["x_center"], each["y_center"])) == True:
						print("Is in red area!!!!!!!!!!!!!")
						flag_valid = True
					else :
						print("Get out of here and Go to red!!")

			if self.layer_mode == 2 or flag_valid == False:
				pnt_prp = self.get_valid_point_in_proper_area(each)
				if pnt_prp != (-1, -1):
					print("움직임?")
					print("each: ")
					print(each)
					tmp_height = self.get_height_layer(self.layer_mode)
					# self.run_point(self.move, [target_point[0], target_point[1], tmp_height+30, 115])
					self.run_point(self.move, [target_point[0], target_point[1], self.get_height_layer(2)+1, 115])
					self.run_point(self.move, [target_point[0], target_point[1], tmp_height, 115])
					self.gripper_DO(self.dashboard, self.gripper_port, 1)
					# self.run_point(self.move, [target_point[0], target_point[1], tmp_height+30, 115])
					self.run_point(self.move, [target_point[0], target_point[1],self.get_height_layer(self.layer_mode + 1)+1, 115])

					self.run_point(self.move, [pnt_prp[0], pnt_prp[1], self.get_height_layer(self.layer_mode + 1)+1, 115])
					# self.run_point(self.move, [pnt_prp[0], pnt_prp[1], self.get_height_layer(2)+2, 115])
					self.run_point(self.move, [pnt_prp[0], pnt_prp[1], self.get_height_layer(1)+1, 115])
					self.gripper_DO(self.dashboard, self.gripper_port, 0)
					self.run_point(self.move, [pnt_prp[0], pnt_prp[1], self.get_height_layer(self.layer_mode + 1)+1, 115])
					self.run_point(self.move, point_home)
					sleep(3.5)
				else:
					print("못 가 히히! 점 없어!")
					is_all_valid = False
					continue
				is_all_valid = False
				if self.layer_mode != 2:
					break

		# sleep(1000)
		
		if len(self.curr_blocks) >= 2 and self.layer_mode == 2:
			self.layer_mode = 1

		self.curr_blocks.clear()
		self.run_point(self.move, point_home)
		sleep(2)

		if is_all_valid == True:
			print("Is All Valid!!! I'm Done!")
			sleep(20)
			self.shutdown()
			exit()


def main(args=None):
	rp.init(args=args)
	yolo_subscriber =YOLOsubscriber()
	
	try:
		rp.spin(yolo_subscriber)
	finally:
		print("Hello finally")
		yolo_subscriber.shutdown()
		# dashboard.DisableRobot()
	rp.shutdown()

if __name__ == "__main__":
	main()