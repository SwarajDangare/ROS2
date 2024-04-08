import rclpy
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='basic_node',
            namespace='ns1',
            executable='number_publisher',
            name='number_publisher',
            arguments=['--ros-args', '--log-level', 'fatal'],
        ),
        Node(
            package='basic_node',
            name='number_counter',
            namespace='ns1',
            executable='number_counter',
            arguments=['--ros-args', '--log-level', 'fatal'],
        )
    ])