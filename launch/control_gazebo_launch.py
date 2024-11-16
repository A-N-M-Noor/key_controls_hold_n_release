# Can't use this because it doesn't give access to the terminal for keyboard input

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    control = Node(
        package='key_controls',
        executable='control',
        name='control',
    )

    ld.add_action(control)

    return ld