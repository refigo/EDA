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
point_home = [245, 5, 50, 115]
point_zero = [255, 0, 0, 115]
point_grip = [304, 19, -25, 16]
point_parse = [255, -54, -5, 115]


point_yellow = [237, 102, -57, 115]
point_green = [337, 12, -57, 115]
point_red = [247, -103, -57, 116]


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
		self.phase = 0
		self.red_stat = 0
		self.yellow_stat = 0
		self.green_stat = 0
		self.pose_stack = Stack()
		self.is_prog = False
		self.x_c = 0.0
		self.y_c = 0.0


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
		y_r = -135 + 285 / 640 * x_i # 284
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
		sleep(5)

	def run_phase_1_logic(self):
		print("nop!")

	def get_height_curr(self):
		ret = 0
		stat_sum = self.red_stat + self.green_stat + self.yellow_stat
		if self.phase == 0:
			if stat_sum == 0:
				ret = -27
			elif stat_sum == 1:
				ret = -44
			elif stat_sum == 2:
				ret = -60
		return ret

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
		pose_yellow = [237, 102]
		pose_green = [337, 12]
		pose_red = [247, -103]
		if str_clr == "red":
			ret_pose = pose_red
		elif str_clr == "green":
			ret_pose = pose_green
		elif str_clr == "yellow":
			ret_pose = pose_yellow
		return ret_pose

	def camera_callback(self, msg):
		self.img = cv_bridge.imgmsg_to_cv2(msg, "bgr8")
		return
		if self.img is not None:
			cv2.imshow('Yolo detections', self.img)
			cv2.waitKey(1)


	def yolo_callback(self,msg):
		print("야 도냐?")
		print("[status]")
		print(f"red_stat: {self.red_stat}")
		print(f"yellow_stat: {self.yellow_stat}")
		print(f"green_stat: {self.green_stat}")
		print(f"is_prog: {self.is_prog}")
		print(f"phase: {self.phase}")
		# return
		for result in msg.yolov8_inference:

			class_name = result.label
			top = result.top
			top_left = result.top_left
			bottom = result.bottom
			bottom_right = result.bottom_right
			conf = round(result.conf, 2)
			# self.get_logger().info(f"{class_name} : {top}, {top_left}, {bottom}, {bottom_right} / {conf}")

			if self.x_c == 0.0 and self.y_c == 0.0:
				y_i = (top_left + bottom_right) / 2
				x_i = (top + bottom) / 2
				self.x_c = x_i
				self.y_c = y_i


			if self.phase == 0:
				if (class_name == "red" and self.red_stat == 0 and self.is_prog == False):
					self.is_prog = True
					# x_r, y_r = self.trans_img_to_rbt(x_i, y_i)
					x_r, y_r = self.trans_img_to_rbt(self.x_c, self.y_c)
					# Move to grip
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					self.run_point(self.move, [x_r, y_r, self.get_height_curr()+8, 115])
					self.run_point(self.move, [x_r, y_r, self.get_height_curr(), 115])
					# self.wait_arrive([x_r, y_r, self.get_height_curr(), 115])
					# Grip
					# sleep(1)
					self.gripper_DO(self.dashboard, self.gripper_port, 1)
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					# sleep(1)
					# Move to put
					self.run_point(self.move, [point_red[0], point_red[1], self.get_height_curr()+5, 115])
					self.run_point(self.move, point_red)
					# Put and up
					# sleep(1)
					self.gripper_DO(self.dashboard, self.gripper_port, 0)
					# sleep(1)
					# self.run_point(self.move, [point_red[0], point_red[1], 0, 115])
					sleep(2)
					self.pose_stack.push("red")
					self.red_stat = 1
					# self.run_point(self.move, point_home)
					# sleep(1)
					self.is_prog = False
				elif (class_name == "yellow" and self.yellow_stat == 0 and self.is_prog == False):
					self.is_prog = True
					# x_r, y_r = self.trans_img_to_rbt(x_i, y_i)
					x_r, y_r = self.trans_img_to_rbt(self.x_c, self.y_c)
					# Move to grip
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					self.run_point(self.move, [x_r, y_r, self.get_height_curr()+8, 115])
					self.run_point(self.move, [x_r, y_r, self.get_height_curr(), 115])
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					# Grip
					# sleep(1)
					self.gripper_DO(self.dashboard, self.gripper_port, 1)
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					# sleep(1)
					# Move to put
					self.run_point(self.move, [point_yellow[0], point_yellow[1], self.get_height_curr()+5, 115])
					self.run_point(self.move, point_yellow)
					# Put and up
					# sleep(1)
					self.gripper_DO(self.dashboard, self.gripper_port, 0)
					# sleep(1)
					# self.run_point(self.move, [point_yellow[0], point_yellow[1], 0, 115])
					sleep(2)
					self.pose_stack.push("yellow")
					self.yellow_stat = 1
					# self.run_point(self.move, point_home)
					# sleep(1)
					self.is_prog = False
				elif (class_name == "green" and self.green_stat == 0 and self.is_prog == False):
					self.is_prog = True
					# x_r, y_r = self.trans_img_to_rbt(x_i, y_i)
					x_r, y_r = self.trans_img_to_rbt(self.x_c, self.y_c)
					# Move to grip
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					self.run_point(self.move, [x_r, y_r, self.get_height_curr()+8, 115])
					self.run_point(self.move, [x_r, y_r, self.get_height_curr(), 115])
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					# Grip
					# sleep(1)
					self.gripper_DO(self.dashboard, self.gripper_port, 1)
					# self.run_point(self.move, [x_r, y_r, 0, 115])
					# sleep(1)
					# Move to put
					self.run_point(self.move, [point_green[0], point_green[1], self.get_height_curr()+5, 115])
					self.run_point(self.move, point_green)
					# Put and up
					# sleep(1)
					self.gripper_DO(self.dashboard, self.gripper_port, 0)
					# sleep(1)
					# self.run_point(self.move, [point_green[0], point_green[1], 0, 115])
					sleep(2)
					self.pose_stack.push("green")
					self.green_stat = 1
					# self.run_point(self.move, point_home)
					# sleep(1)
					self.is_prog = False
				# sleep(1)

				
		if self.red_stat == 1 and self.yellow_stat == 1 and self.green_stat == 1 and self.is_prog == False:
			# self.run_point(self.move, point_home)
			self.phase = 1
			# sleep(5)
			# raise Exception("Done Phase 1")

			# if self.img is not None:
			# 	cv2.rectangle(self.img, (top, top_left), (bottom, bottom_right), (255, 255, 0))
			# 	cv2.putText(self.img, f"{class_name} : {conf:.2f}", (top, top_left), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (255, 0, 255), 2)
		if self.phase == 1 and self.is_prog == False:
			self.phase = 2
			self.is_prog = True
			print("In phase 1")
			base_pos = self.get_color_pose(self.pose_stack.pop())
			cur_pose = self.get_color_pose(self.pose_stack.pop())
			print(f"cur_pose: {cur_pose}")
			# middle
			test = self.get_height_layer(1)
			print(f"get_height_layer(1): {test}")
			self.run_point(self.move, [cur_pose[0], cur_pose[1], self.get_height_layer(1)+1, 115])
			self.gripper_DO(self.dashboard, self.gripper_port, 1)
			self.run_point(self.move, [base_pos[0], base_pos[1], self.get_height_layer(2)+20, 115])
			self.run_point(self.move, [base_pos[0], base_pos[1], self.get_height_layer(2), 115])
			self.gripper_DO(self.dashboard, self.gripper_port, 0)
			self.run_point(self.move, [base_pos[0], base_pos[1], self.get_height_layer(2)+8, 115])
			sleep(2)
			# top
			cur_pose = self.get_color_pose(self.pose_stack.pop())
			self.run_point(self.move, [cur_pose[0], cur_pose[1], self.get_height_layer(1)+1, 115])
			self.gripper_DO(self.dashboard, self.gripper_port, 1)
			self.run_point(self.move, [base_pos[0], base_pos[1], self.get_height_layer(3)+20, 115])
			self.run_point(self.move, [base_pos[0], base_pos[1], self.get_height_layer(3), 115])
			self.gripper_DO(self.dashboard, self.gripper_port, 0)
			# self.run_point(self.move, [base_pos[0], base_pos[1], self.get_height_layer(3) + 20, 115])
			self.run_point(self.move, point_home)
			sleep(20)
			self.phase = 2
			self.is_prog = False

		if self.phase == 2 and self.is_prog == False:
			self.dashboard.DisableRobot()




		# if self.phase == 0:
		# 	self.run_phase_0_logic()

		# if self.phase == 1:
		# 	self.run_phase_1_logic()

		# if self.img is not None:
		# 	cv2.imshow('Yolo detections', self.img)
		# 	cv2.waitKey(1)


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