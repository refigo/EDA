import threading
from yolo_pkg.dobot_api import DobotApiDashboard, DobotApi, DobotApiMove, MyType
from time import sleep

import numpy as np
# 전역 변수 (현재 좌표)
current_actual = None



# 로봇이 이동하고자 하는 좌표 (x, y, z, yaw) unit : mm, degree
point_home = [245, 5, 50, 115]
point_zero = [255, 0, 0, 115]
point_grip = [304, 19, -25, 16]
point_parse = [255, -54, -5, 115]


class DobotExecutor(Node):
	def __init__(self):
		super().__init__("dobot_executor")


		# print("tq")
		# 입력 파라미터
		self.ip = "192.168.1.6" # Robot의 IP 주소
		self.gripper_port = 1   # 그리퍼 포트 번호
		self.speed_value = 100   # 로봇 속도 (1~100 사이의 값 입력)

		# 로봇 연결
		self.dashboard, self.move, self.feed = self.connect_robot(self.ip)
		self.dashboard.EnableRobot()
		print("이제 로봇을 사용할 수 있습니다!")


		# 쓰레드 설정
		self.feed_thread = threading.Thread(target=get_feed, args=(self.feed,))
		self.feed_thread.setDaemon(True)
		self.feed_thread.start()
		# 전역 변수 (현재 좌표)
		self.current_actual = None# 로봇 상태 초기화 1 : 로봇 에러 메시지 초기화
		self.robot_clear(self.dashboard)
		# 로봇 상태 초기화 2 : 로봇 속도 조절
		self.robot_speed(self.dashboard, self.speed_value)
		# 로봇 현재 위치 받아오기 (x, y, z, yaw) - 로봇 베이스 좌표계
		self.get_Pose(self.dashboard)

		# sleep(5)


	def connect_robot(ip):
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

	def robot_clear(dashboard : DobotApiDashboard):
		dashboard.ClearError()
		
	def robot_speed(dashboard : DobotApiDashboard, speed_value):
		dashboard.SpeedFactor(speed_value)

	def gripper_DO(dashboard : DobotApiDashboard, index, status):
		dashboard.ToolDO(index, status)
		
	def get_Pose(dashboard : DobotApiDashboard):
		dashboard.GetPose()
		
	def run_point(move: DobotApiMove, point_list: list):
		move.MovL(point_list[0], point_list[1], point_list[2], point_list[3])
		
	def get_feed(feed: DobotApi):
		global current_actual
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
				current_actual = a["tool_vector_actual"][0] # Refresh Properties
			sleep(0.001)
			
	def wait_arrive(point_list):
		global current_actual
		while True:
			is_arrive = True
			if current_actual is not None:
				for index in range(4):
					if (abs(current_actual[index] - point_list[index]) > 1):
						is_arrive = False
				if is_arrive:
					return
			sleep(0.001)


	def trans_img_to_rbt(x_i, y_i):
		x_r = 186 + 196 / 480 * y_i
		y_r = -142 + 284 / 640 * x_i
		return (x_r, y_r)



def main(args=None):
	rp.init(args=args)
	dobot_executor =DobotExecutor()
	rp.spin(dobot_executor)
	rp.shutdown()


if __name__ == "__main__":
	main()