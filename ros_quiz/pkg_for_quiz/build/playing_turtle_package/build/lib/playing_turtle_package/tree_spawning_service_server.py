from playing_turtle_package_msgs.srv import TreeSpawn
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn

import time
import rclpy as rp
import numpy as np
from rclpy.node import Node

class TreeSpawning(Node):

	def __init__(self):
		super().__init__('tree_spawn')
		self.server = self.create_service(TreeSpawn, 'tree_spawn', self.callback_service)
		self.teleport = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
		self.spawn = self.create_client(Spawn, '/spawn')
		self.req_teleport = TeleportAbsolute.Request()
		self.req_spawn = Spawn.Request()
		self.center_x = 5.54
		self.center_y = 5.54

	def callback_service(self, request, response):
		print('request: ', request)

		self.req_spawn.x = 0 + self.center_x
		self.req_spawn.y = 3 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)

		self.req_spawn.x = 1 + self.center_x
		self.req_spawn.y = 1 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)

		self.req_spawn.x = -1 + self.center_x
		self.req_spawn.y = 1 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)


		self.req_spawn.x = 1 + self.center_x
		self.req_spawn.y = -2 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)

		self.req_spawn.x = -1 + self.center_x
		self.req_spawn.y = -2 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)

		self.req_spawn.x = 0.5 + self.center_x
		self.req_spawn.y = -3 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)
		self.req_spawn.x = -0.5 + self.center_x
		self.req_spawn.y = -3 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)

		self.req_spawn.x = 0.5 + self.center_x
		self.req_spawn.y = -4 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)
		self.req_spawn.x = -0.5 + self.center_x
		self.req_spawn.y = -4 + self.center_y
		self.spawn.call_async(self.req_spawn)
		time.sleep(0.01)

		response.x = []
		response.y = []
		response.theta = []

		return response

def main(args=None):
	rp.init(args=args)
	tree_spawn = TreeSpawning()
	rp.spin(tree_spawn)
	rp.shutdown()

if __name__ == '__main__':
	main()
