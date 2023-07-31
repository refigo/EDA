import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from pathlib import Path

def generate_launch_description():
    pkg_share = get_package_share_directory('aruco_pkg')
    aruco_detect_node = os.path.join(pkg_share, 'src', 'aruco_5_recognition_node.py')
    camera_publisher_node = os.path.join(pkg_share, 'src', 'img_pub.py')

    marker_size = LaunchConfiguration('marker_size', default='3.5')

    marker_size_arg = DeclareLaunchArgument(
        'marker_size',
        default_value='3.5',
        description='Marker_Size'
    )

    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('aruco_pkg'),
        'params',
        'aruco_config.yaml'
        )
    )

    return LaunchDescription(
        [
            marker_size_arg,
            Node(
                package='aruco_pkg',
                executable='image_publisher',
                name='image_publisher',
                parameters=[param_dir],
                output='screen'
            ),
            Node(
                package='aruco_pkg',
                executable='marker_4X4_recognition',
                name='marker_4',
                parameters=[param_dir, {'marker_size': marker_size}],
                output='screen'
            ),
            Node(
                package='aruco_pkg',
                executable='marker_5X5_recognition',
                name='marker_5',
                parameters=[param_dir, {'marker_size': marker_size}],
                output='screen'
            ),
            Node(
                package='aruco_pkg',
                executable='marker_6X6_recognition',
                name='marker_6',
                parameters=[param_dir, {'marker_size': marker_size}],
                output='screen'
            ),
            Node(
                package='aruco_pkg',
                executable='marker_7X7_recognition',
                name='marker_7',
                parameters=[param_dir, {'marker_size': marker_size}],
                output='screen'
            ),

        ]
        )