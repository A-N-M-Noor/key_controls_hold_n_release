# Key Controls for TurtleBot3

This package provides key controls for the TurtleBot3 robot.

## Installation

Clone the repository into your workspace:

```bash
cd ~/turtlebot3_ws/src
git clone https://github.com/yourusername/key_controls.git
```

Build the package using colcon:

```bash
cd ~/turtlebot3_ws
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

## Usage

To run the key controls node, use the following command:

```bash
ros2 run key_controls control
```

To run the serial communication node, use the following command:

```bash
ros2 run key_controls serial_node
```

## Dependencies

Ensure you have the following dependencies installed:

- ROS 2 (Robot Operating System)
- TurtleBot3 packages

## Acknowledgments

- [TurtleBot3](https://www.turtlebot.com/turtlebot3/) for providing the robot platform.

