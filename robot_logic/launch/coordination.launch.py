from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='robot_logic', executable='detector_node', name='detector_node', parameters=[{'x': 0.5}]),
        Node(package='robot_logic', executable='center_node', name='center_node'),
        Node(package='robot_logic', executable='executor_node', name='executor_node'),
        Node(package='tf2_ros', executable='static_transform_publisher', arguments=['1.0', '0', '0.5', '0', '0', '0', 'map', 'camera_link'])
    ])
