import cv2
import rclpy as rp
import numpy as np
import logging

from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped, PoseArray
from rcl_interfaces.msg import ParameterDescriptor, ParameterType
from visualization_msgs.msg import Marker, MarkerArray
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
from tf_transformations import quaternion_from_matrix

class MarkerDetector(Node):

    def __init__(self):
        super().__init__('marker_5x5_node')
        self.distance = 0.0
        self.x = 0.0
        self.y = 0.0
        self.cv_bridge = CvBridge()

        self.calibration_path = get_package_share_directory('aruco_pkg') + '/params/camera_calibration.npz'
        self.calib_data = np.load(self.calibration_path)
        self.cam_mat = self.calib_data["camera_matrix"]
        self.dist_coef = self.calib_data["distortion_coefficients"]
        self.r_vectors = self.calib_data["rvecs"]
        self.t_vectors = self.calib_data["tvecs"]

        self.declare_parameter('marker_size', 3.5, 
descriptor=ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE))
        self.marker_size = self.get_parameter('marker_size').value
        self.get_logger().info(f"Marker Size : {self.marker_size}")

        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_250)
        self.aruco_params = cv2.aruco.DetectorParameters_create()

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("marker_5x5_node")

        self.camera_sub = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            10
        )
        
        self.pose_publisher = self.create_publisher(MarkerArray, 'marker_pose', 10)
    
    #convert from 3x3 matrix to quaternion
#     def rotation_matrix_to_quaternion(self, rot_matrix):
#         trace = rot_matrix[0, 0] + rot_matrix[1, 1] + rot_matrix[2, 2]
#         if trace > 0:
#             S    = 0.5 * np.sqrt(trace + 1.0)
#             qw = 0.25 * S
#             qx = (rot_matrix[2, 1] - rot_matrix[1, 2]) / S
#             qy = (rot_matrix[0, 2] - rot_matrix[2, 0]) / S
#             qz = (rot_matrix[1, 0] - rot_matrix[0, 1]) / S
#         elif (rot_matrix[0, 0] > rot_matrix[1, 1]) and (rot_matrix[0, 0] >
# rot_matrix[2, 2]):
#             S = np.sqrt(1.0 + rot_matrix[0, 0] - rot_matrix[1, 1] - rot_matrix[2, 2]) * 2
#             qw = (rot_matrix[2, 1] - rot_matrix[1, 2]) / S
#             qx = 0.25 * S
#             qy = (rot_matrix[0, 1] + rot_matrix[1, 0]) / S
#             qz = (rot_matrix[0, 2] + rot_matrix[2, 0]) / S
#         elif rot_matrix[1, 1] > rot_matrix[2, 2]:
#             S = np.sqrt(1.0 + rot_matrix[1, 1] - rot_matrix[0, 0] - rot_matrix[2, 2]) * 2
#             qw = (rot_matrix[0, 2] - rot_matrix[2, 0]) / S
#             qx = (rot_matrix[0, 1] + rot_matrix[1, 0]) / S
#             qy = 0.25 * S
#             qz = (rot_matrix[1, 2] + rot_matrix[2, 1]) / S
#         else:
#             S = np.sqrt(1.0 + rot_matrix[2, 2] - rot_matrix[0, 0] - rot_matrix[1, 1]) * 2
#             qw = (rot_matrix[1, 0] - rot_matrix[0, 1]) / S
#             qx = (rot_matrix[0, 2] + rot_matrix[2, 0]) / S
#             qy = (rot_matrix[1, 2] + rot_matrix[2, 1]) / S
#             qz = 0.25 * S

#         return np.array([qw, qx, qy, qz])

    def image_callback(self, msg):
        if msg is None:
            self.get_logger().warn("No Camera Data has been received!")
        cv_image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')
        
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = cv2.aruco.detectMarkers(gray, self.aruco_dict,
parameters=self.aruco_params)

        pose_array = PoseArray()

        marker_array = MarkerArray()

        if corners:
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                corners, self.marker_size, self.cam_mat, self.dist_coef
            )

            total_markers = range(0, ids.size)

            for id, corner, i in zip(ids, corners, total_markers):

                rotation_matrix, _ = cv2.Rodrigues(rvecs[0])

                self.get_logger().info(f"R : {rotation_matrix}")

                transform_matrix = np.eye(4)
                transform_matrix[:3, :3] = rotation_matrix
                
                # quaternion = self.rotation_matrix_to_quaternion(rotation_matrix)
                quaternion = quaternion_from_matrix(transform_matrix)
                pose_msg = PoseStamped()
                pose_msg.header.stamp = self.get_clock().now().to_msg()
                # pose_msg.header.frame_id = 'marker'
                pose_msg.header.frame_id = 'base_link'
                pose_msg.pose.position.x = tvecs[0][0][0]
                pose_msg.pose.position.y = tvecs[0][0][1]
                pose_msg.pose.position.z = tvecs[0][0][2]

                # pose_msg.pose.orientation.x = quaternion[1]
                # pose_msg.pose.orientation.y = quaternion[2]
                # pose_msg.pose.orientation.z = quaternion[3]
                # pose_msg.pose.orientation.w = quaternion[0]
                pose_msg.pose.orientation.x = quaternion[0]
                pose_msg.pose.orientation.y = quaternion[1]
                pose_msg.pose.orientation.z = quaternion[2]
                pose_msg.pose.orientation.w = quaternion[3]
                
                pose_array.header = pose_msg.header

                pose_array.poses.append(pose_msg.pose)
                # self.pose_publisher.publish(pose_array)

                marker_msg = Marker()
                marker_msg.header.frame_id = pose_msg.header.frame_id
                marker_msg.header.stamp = pose_msg.header.stamp
                marker_msg.id = int(id[0])
                marker_msg.type = Marker.TEXT_VIEW_FACING
                marker_msg.pose = pose_msg.pose
                marker_msg.scale.z = 0.05
                marker_msg.color.r = 1.0
                marker_msg.color.g = 1.0
                marker_msg.color.b = 1.0
                marker_msg.color.a = 1.0

                marker_array.markers.append(marker_msg)


                cv2.polylines(
                    cv_image, [corner.astype(np.int32)], True, (0, 255, 255), 2,
cv2.LINE_AA
                )
                corner = corner.reshape(4,2)
                corner = corner.astype(int)
                top_right = corner[0].ravel()
                top_left = corner[1].ravel()
                bottom_right = corner[2].ravel()
                bottom_left = corner[3].ravel()

                self.distance = np.sqrt(
                    tvecs[i][0][0] ** 2 + tvecs[i][0][1] ** 2 + tvecs[i][0][2] ** 2
                )


                # Draw the pose of the marker
                point = cv2.drawFrameAxes(cv_image, self.cam_mat, self.dist_coef,
rvecs[i], tvecs[i], 4, 4)

                cv2.putText(
                    cv_image,
                    f"id: {id[0]} Dist: {round(self.distance, 2)}",
                    top_right,
                    cv2.FONT_HERSHEY_PLAIN,
                    1.3,
                    (0, 0, 255),
                    2,
                    cv2.LINE_AA,
                )

                cv2.putText(
                    cv_image,
                    f"x:{round(tvecs[i][0][0],1)} y: {round(tvecs[i][0][1],1)} ",
                    bottom_right,
                    cv2.FONT_HERSHEY_PLAIN,
                    1.0,
                    (0, 0, 255),
                    2,
                    cv2.LINE_AA,
                )
                self.x, self.y = round(tvecs[i][0][0],1), round(tvecs[i][0][1],1)

            self.pose_publisher.publish(marker_array)

        rgb_cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        cv2.imshow("frame", rgb_cv_image)
        cv2.waitKey(100)



def main(args=None):
    rp.init(args=args)
    node = MarkerDetector()
    rp.spin(node)
    node.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()