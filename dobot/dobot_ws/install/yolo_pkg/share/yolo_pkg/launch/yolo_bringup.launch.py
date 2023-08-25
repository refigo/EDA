import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
	model_name_arg = DeclareLaunchArgument(
		'model_name',
		default_value='best.pt',
		description="Yolo v8 model to use"
	)

	model_name = LaunchConfiguration('model_name')

	camera_node = Node(
		package='yolo_pkg',
		executable='image_publisher',
		name='image_publisher',
		# output='screen'
	)

	detector_node = Node(
		package='yolo_pkg',
		executable='object_detect_publisher',
		parameters=[{'model_name' : model_name}],
		# output='screen',
	)

	subs_node = Node(
		package='yolo_pkg',
		executable='object_detect_subscriber',
		output='screen'
		)

	return LaunchDescription([
		model_name_arg,
		camera_node,
		detector_node,
		subs_node
	])