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

import cv2

class ObjectDetection(Node):
	def __init__(self):

		super().__init__('object_dectection_node')
		self.cv_bridge = CvBridge()
		self.model_name_param = self.declare_parameter('model_name', 'best.pt')
		self.pkg_share_path = get_package_share_directory('yolo_pkg')
		self.model_dir = os.path.join(self.pkg_share_path, 'models')
		self.model_name = self.model_name_param.value
		self.model_path = os.path.join(self.model_dir, self.model_name)
		self.model = YOLO(self.model_path)
		# self.get_logger().info(f"model : {self.model_path}")

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
		self.img = None


	def camera_callback(self, msg):
		self.img = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")

		img = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
		results = self.model(img)

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

				class_name = self.inference_result.label
				top = self.inference_result.top
				top_left = self.inference_result.top_left
				bottom = self.inference_result.bottom
				bottom_right = self.inference_result.bottom_right
				conf = round(self.inference_result.conf, 2)
				if self.img is not None:
					cv2.rectangle(self.img, (top, top_left), (bottom, bottom_right), (255, 255, 0))
					cv2.putText(self.img, f"{class_name} : {conf:.2f}", (top, top_left), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (255, 0, 255), 2)


		annotated_frame = results[0].plot()
		img_msg = self.cv_bridge.cv2_to_imgmsg(annotated_frame)

		self.img_pub.publish(img_msg)
		self.yolov8_pub.publish(self.yolov8_inference)
		self.yolov8_inference.yolov8_inference.clear()

		if self.img is not None:
			cv2.imshow('Yolo detections', self.img)
			cv2.waitKey(1)




def main(args=None):
	rp.init(args=args)
	objectdetection = ObjectDetection()
	rp.spin(objectdetection)
	rp.shutdown()


if __name__ == "__main__":
	main()