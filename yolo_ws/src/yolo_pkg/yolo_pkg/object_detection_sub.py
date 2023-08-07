import rclpy as rp
import cv2
import threading

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from yolo_inference.msg import Yolov8Inference

cv_bridge = CvBridge()
img = None

class YOLOsubscriber(Node):
	def __init__(self):
		super().__init__("yolo_subscriber")

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

	def camera_callback(self, msg):
		self.img = cv_bridge.imgmsg_to_cv2(msg, "bgr8")

	def yolo_callback(self,msg):
		for result in msg.yolov8_inference:

			class_name = result.label
			top = result.top
			top_left = result.top_left
			bottom = result.bottom
			bottom_right = result.bottom_right
			conf = round(result.conf, 2)
			self.get_logger().info(f"{class_name} : {top}, {top_left}, {bottom}, {bottom_right} / {conf}")

			if self.img is not None:
				cv2.rectangle(self.img, (top, top_left), (bottom, bottom_right), (255, 255, 0))
				cv2.putText(self.img, f"{class_name} : {conf:.2f}", (top, top_left), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (255, 0, 255), 2)

		if self.img is not None:
			cv2.imshow('Yolo detections', self.img)
			cv2.waitKey(1)


def main(args=None):
	rp.init(args=args)
	yolo_subscriber =YOLOsubscriber()
	rp.spin(yolo_subscriber)
	rp.shutdown()


if __name__ == "__main__":
	main()