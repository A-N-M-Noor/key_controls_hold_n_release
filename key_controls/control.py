import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, termios, tty

import threading

from time import time

class ControlNode(Node):
    def __init__(self):
        super().__init__('control')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info('Control node has been started.\n')
        self.get_logger().info(
            f"""
Control your robot with the following keys:

            w
        a       d
            s

press q to exit."""
            )
        
        self.pressed_key = None

        self.linSpd = 0.5
        self.angSpd = 0.25

        self.timer = time()
        self.timeOut = 0.5

        self.pubTimer = self.create_timer(0.2, self.publish_twist)
        self.running = True

        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def publish_twist(self):
        if(time() - self.timer > self.timeOut):
            self.pressed_key = None

        twist = Twist()
        if(self.pressed_key == 'w'):
            twist.linear.x = self.linSpd
        elif(self.pressed_key == 's'):
            twist.linear.x = -self.linSpd
        elif(self.pressed_key == 'a'):
            twist.angular.z = self.angSpd
        elif(self.pressed_key == 'd'):
            twist.angular.z = -self.angSpd
        
        self.publisher.publish(twist)

        if(not self.running):
            self.get_logger().info('Exiting control node.')
            sys.exit()

    def run(self):
        try:
            while True:
                key = self.get_key()

                if key == '\x03' or key == 'q':
                    break
                    
                else:
                    self.pressed_key = key
                    self.timer = time()
                sys.stdout.flush()

        except Exception as e:
            self.get_logger().error(f'Exception: {e}')
        
        finally:
            self.running = False
            self.pressed_key = None
            sys.exit()

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()