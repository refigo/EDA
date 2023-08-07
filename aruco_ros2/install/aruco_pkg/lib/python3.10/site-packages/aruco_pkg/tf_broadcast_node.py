import rclpy as rp
import tf2_ros

from rclpy.duration import Duration
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from visualization_msgs.msg import MarkerArray


class MarkerTFBroadcaster(Node):
	def __init__(self):
		super().__init__('marker_tf_broadcaster')

		self.marker_sub = self.create_subscription(
			MarkerArray,
			'/marker_pose',
			self.marker_callback,
			10
		)
		self.tf_buffer = tf2_ros.Buffer()
		self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
		self.br = tf2_ros.TransformBroadcaster(self)

	def marker_callback(self, msg):
		transforms = []
		for marker in msg.markers:
			tf = TransformStamped()
			tf.header.stamp = self.get_clock().now().to_msg()

			tf.header.frame_id = "base_link"
			tf.child_frame_id = "marker" + str(marker.id)
			tf.transform.translation.x = marker.pose.position.x * 0.1
			tf.transform.translation.y = marker.pose.position.y * 0.1
			tf.transform.translation.z = marker.pose.position.z * 0.1

			tf.transform.rotation.x = marker.pose.orientation.x
			tf.transform.rotation.y = marker.pose.orientation.y
			tf.transform.rotation.z = marker.pose.orientation.z
			tf.transform.rotation.w = marker.pose.orientation.w

			transforms.append(tf)

			try:
				when = self.get_clock().now() - Duration(seconds=1.0)
				trans = self.tf_buffer.lookup_transform('base_link', "marker" + str(marker.id), when)
				print("Transform llokup succeeded: %s" % trans)
				self.get_logger().info("Transform lookup succeeded: %s" % trans)
			except Exception as e:
				self.get_logger().error("Transform lookup failed: %s" % e)

		self.br.sendTransform(transforms)

def main(args=None):
	rp.init(args=args)
	tf_node = MarkerTFBroadcaster()

	try:
		rp.spin(tf_node)
	except KeyboardInterrupt:
		pass

	tf_node.destroy_node()
	rp.shutdown()

if __name__ == "__main__":
	main()
