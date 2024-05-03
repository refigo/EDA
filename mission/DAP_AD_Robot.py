from nav2_simple_commander.robot_navigator import BasicNavigator

import rclpy as rp
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.duration import Duration

import tf2_ros
from geometry_msgs.msg import TransformStamped
from visualization_msgs.msg import MarkerArray

import time
import cv2
import numpy as np
import logging

from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped, PoseArray
from rcl_interfaces.msg import ParameterDescriptor, ParameterType
from visualization_msgs.msg import Marker, MarkerArray
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
from tf_transformations import quaternion_from_matrix

import rclpy as rp
import numpy as np
import os

from ultralytics import YOLO
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from yolo_inference.msg import InferenceResult
from yolo_inference.msg import Yolov8Inference

from ament_index_python.packages import get_package_share_directory

class ObjectDetection(Node):
    def __init__(self):

        super().__init__('object_dectection_node')
        self.cv_bridge = CvBridge()
        self.model_name_param = self.declare_parameter('model_name', 'yolov8n.pt')
        self.pkg_share_path = get_package_share_directory('yolo_pkg')
        self.model_dir = os.path.join(self.pkg_share_path, 'models')
        self.model_name = self.model_name_param.value
        self.model_path = os.path.join(self.model_dir, self.model_name)
        self.model = YOLO(self.model_path)
        self.get_logger().info(f"model : {self.model_path}")

        self.yolov8_inference = Yolov8Inference()

        self.camera_sub = self.create_subscription(
            Image,
            'image_raw',
            self.camera_callback,
            10
        )
        self.camera_sub

        self.yolov8_pub = self.create_publisher(Yolov8Inference, "/yolov8_inference", 1)
        self.img_pub = self.create_publisher(Image, "/inference_result", 1)
        
        self.img_size = 0
        self.is_detected = False


    def camera_callback(self, msg):
        self.is_detected = False

        img = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        results = self.model(img)
        
        if self.img_size == 0:
            self.img_size = msg.height * msg.width

        self.yolov8_inference.header.frame_id = "inference"
        self.yolov8_inference.header.stamp = self.get_clock().now().to_msg()

        for result in results:
            boxes = result.boxes.data.cpu()
            # box = np.array(boxes)
            for box in boxes:
                self.inference_result = InferenceResult()
                label = int(box[5])
                self.inference_result.label = self.model.names[label]
                self.inference_result.top = int(box[0])
                self.inference_result.top_left = int(box[1])
                self.inference_result.bottom = int(box[2])
                self.inference_result.bottom_right = int(box[3])
                self.inference_result.conf = float(box[4])
                self.yolov8_inference.yolov8_inference.append(self.inference_result)

                each_box_size = (self.inference_result.bottom - self.inference_result.top) * (self.inference_result.bottom_right - self.inference_result.top_left)
                print(f"each_box_size: {each_box_size}")
                print(f"img_size: {self.img_size}")
                print("self.inference_result.label type:", type(self.inference_result.label))
                print(self.inference_result.label)
                if each_box_size / self.img_size >= 0.5 and self.inference_result.label == "person":
                    self.is_detected = True

        annotated_frame = results[0].plot()
        img_msg = self.cv_bridge.cv2_to_imgmsg(annotated_frame)
        self.img_pub.publish(img_msg)
        self.yolov8_pub.publish(self.yolov8_inference)
        self.yolov8_inference.yolov8_inference.clear()


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


pose_stack = Stack()
real_map = [
    [ 0 , 'D', 'D'],
    ['A', 'B', 'C']
]
visited = [
    [0, 0, 0],
    [0, 0, 0]
]


rp.init()

nav = BasicNavigator()

# position A (initial pose)
pos_a = PoseStamped()
pos_a.header.frame_id = 'map'
pos_a.header.stamp = nav.get_clock().now().to_msg()
pos_a.pose.position.x = 0.0
pos_a.pose.position.y = 0.0
pos_a.pose.orientation.z = 0.0
pos_a.pose.orientation.w = 0.0
nav.setInitialPose(pos_a)

pose_stack.push(pos_a)

nav.waitUntilNav2Active()

od = ObjectDetection()

# position B
pos_b = PoseStamped()
pos_b.header.frame_id = 'map'
pos_b.header.stamp = nav.get_clock().now().to_msg()
pos_b.pose.position.x = 1.0
pos_b.pose.position.y = 0.3
pos_b.pose.orientation.w = 0.
pos_b.pose.orientation.z = 0.

# position C
pos_c = PoseStamped()
pos_c.header.frame_id = 'map'
pos_c.header.stamp = nav.get_clock().now().to_msg()
pos_c.pose.position.x = 1.7
pos_c.pose.position.y = 0.
pos_c.pose.orientation.w = 0.
pos_c.pose.orientation.z = 0.

# position D
pos_d = PoseStamped()
pos_d.header.frame_id = 'map'
pos_d.header.stamp = nav.get_clock().now().to_msg()
pos_d.pose.position.x = 1.6
pos_d.pose.position.y = 1.0
pos_d.pose.orientation.w = 0.
pos_d.pose.orientation.z = 0.


def move_to_goal(goal_pos):
    
    goal_pos.header.stamp = nav.get_clock().now().to_msg()
    
    nav.goToPose(goal_pos)

    i = 0
    while not nav.isTaskComplete():
        i = i + 1

        rp.spin_once(od)
        if (od.is_detected == True):
            print("Is detected!!!!!!")
            nav.cancelTask()
            nav.spin(3.14)
            time.sleep(8)
            if pose_stack.is_empty() == False:
                move_to_goal(pose_stack.top())
            if pose_stack.size() > 1:
                pose_stack.pop()
                move_to_goal(pose_stack.top())
            raise Exception("Object Detection!")
        
        feedback = nav.getFeedback()
        if feedback and i % 5 == 0:
            print('Distance remaining: ' + '{:.2f}'.format(
            feedback.distance_remaining) + 'meters.')

            if feedback.distance_remaining <= 0.25 and Duration.from_msg(feedback.navigation_time) > Duration(seconds=5.0):
                nav.cancelTask()
    if nav.isTaskComplete():
        print("nav2 task completed.")

def task1():
    print("[Task 1]")
    print("move to B")
    move_to_goal(pos_b)
    print("spin 90")
    time.sleep(2)
    nav.spin(-1.57)
    time.sleep(6)
    pose_stack.push(pos_b)

def task2():
    print("[Task 2]")
    print("move to C")
    move_to_goal(pos_c)
    print("spin 360")
    time.sleep(2)
    nav.spin(6.28)
    time.sleep(10)
    pose_stack.push(pos_c)

def task3():
    print("move to D")
    move_to_goal(pos_d)
    print("The End...")
    pose_stack.push(pos_d)


pos_0 = PoseStamped()
pos_0.header.frame_id = 'map'
pos_0.header.stamp = nav.get_clock().now().to_msg()
pos_0.pose.position.x = 0.35
pos_0.pose.position.y = 0.
pos_0.pose.orientation.w = 0.
pos_0.pose.orientation.z = 0.
move_to_goal(pos_0)

while True:
    try:
        task1()
    except Exception as e:
        print(e)
        continue
    break

while True:
    try:
        task2()
    except Exception as e:
        print(e)
        continue
    break

while True:
    try:
        task3()
    except Exception as e:
        print(e)
        continue
    break
