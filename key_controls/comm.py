import serial
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SerialNode(Node):
    def __init__(self):
        super().__init__('serial_node')
        self.ser = None

        while True:
            try:
                self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                break
            except:
                self.get_logger().info('Serial port not available. Retrying...')

        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 2)
        self.create_timer(0.1, self.readSerial)

    def readSerial(self):
        while(self.ser.in_waiting > 0):
            data = self.ser.read_until('\n').decode('utf-8')
            self.get_logger().info(data)

    def listener_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z
        
        send = 0
        if(linear == 0 and angular == 0):
            send = 0
        elif(linear > 0):
            send = 1
        elif(linear < 0):
            send = 2
        elif(angular > 0):
            send = 3
        elif(angular < 0):
            send = 4

        self.ser.write(send.to_bytes(1, 'little'))

def main(args=None):
    rclpy.init(args=args)
    serial_node = SerialNode()
    rclpy.spin(serial_node)
    serial_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()