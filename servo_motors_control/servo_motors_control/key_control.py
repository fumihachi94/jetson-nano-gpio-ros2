import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8
from getch import getch

class key_control(Node):
    def __init__(self):
        super().__init__('key_control')
        self.count = 0
        action = 255
        self.publisher = self.create_publisher(UInt8, '/action')
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.count += 1
        msg = UInt8()
        action_list = {'97': 10, '119': 0, '100': 20, '115': 1, '32': 255}
        key = ord(getch())
        if str(key) in action_list:
            self.action = action_list[str(key)]
            print('key : {}, action : {}'.format(key, self.action))
        else:
            print('Please press key : A W D S Space')

        msg.data = self.action
        self.publisher.publish(msg)

def main():
    rclpy.init()
    key_control_node = key_control()
    rclpy.spin(key_control_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()