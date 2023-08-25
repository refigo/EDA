import rclpy as rp
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class WebcamPublisher(Node):
	def __init__(self):
		super().__init__('camera_publisher')
		self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
		self.bridge = CvBridge()

		#set up video capture
		self.capture = cv2.VideoCapture(0) # 카메라 번호
		self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
		self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

		timer_period = 0.02 # seconds\
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def capture_frame(self):
		ret, frame = self.capture.read()
		if not ret:
			# self.get_logger().warning('Failed to capture frame frome camera')
			return None
		return frame

	def publish_frame(self, frame):
		ros_image = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
		self.publisher_.publish(ros_image)
		# self.get_logger().info('Published image')

	def timer_callback(self):
		# Capture a frame from the camera
		frame = self.capture_frame()
		if frame is None:
			return
		# publish the frame as an image message
		self.publish_frame(frame)


def main(args=None):
	rp.init(args=args)
	webcam_publisher = WebcamPublisher()
	rp.spin(webcam_publisher)
	webcam_publisher.destroy_node()
	rp.shutdown()

if __name__ == '__main__':
	main()