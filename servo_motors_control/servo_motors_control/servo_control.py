import rclpy
from rclpy.node import Node
#import sensor_msgs.msg as msg
from std_msgs.msg import UInt8
import time
import Adafruit_PCA9685
import rclpy.qos as qos

class servo_control(Node):
    def __init__(self):
        super().__init__('servo_control')
        profile = qos.QoSProfile()
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        print('Moving servo on channel 0, press Ctrl-C to quit...')
        self.subscription = self.create_subscription(
          UInt8(), '/action', self.control_callback, qos_profile=profile)

    def __del__(self):
        self.pwm.set_pwm(0,0,0)
        self.pwm.set_pwm(1,0,0)
        print('Finish!')

    def control_callback_test(self, msg):
        servo_min = msg.data
        servo_max = int(4096*60.0/1000000.0 * 2300) #430
        print("msg.data: {}, min : {}, max : {}".format(msg.data, servo_min, servo_max))
        self.pwm.set_pwm(0, 0, servo_min)
        self.pwm.set_pwm(1, 0, servo_min)

    def control_callback(self, msg):
        servo_stop_L = 386  # (palse width : 1580μs)
        servo_stop_R = 376  # (palse width : 1530μs)
        servo_min_L  = servo_stop_L - 50
        servo_max_L  = servo_stop_L + 50
        servo_min_R  = servo_stop_R - 50 
        servo_max_R  = servo_stop_R + 50 
        print("msg.data: {}, min : {}, max : {}".format(msg.data, servo_min_L, servo_max_L))
        if msg.data == 0: # Forward-Straight
          self.pwm.set_pwm(0, 0, servo_max_L)
          self.pwm.set_pwm(1, 0, servo_min_R)
        elif msg.data == 10: # Forward-Left
          self.pwm.set_pwm(0, 0, 0)
          self.pwm.set_pwm(1, 0, servo_min_R)
        elif msg.data == 20: # Forward-Right
          self.pwm.set_pwm(0, 0, servo_max_L)
          self.pwm.set_pwm(1, 0, 0)
        elif msg.data == 11: # Backward-Left
          self.pwm.set_pwm(0, 0, 0)
          self.pwm.set_pwm(1, 0, servo_max_R)
        elif msg.data == 21: # Backward-Right
          self.pwm.set_pwm(0, 0, servo_min_L)
          self.pwm.set_pwm(1, 0, 0)
        elif msg.data == 1: # Backward-Straight
          self.pwm.set_pwm(0, 0, servo_min_L)
          self.pwm.set_pwm(1, 0, servo_max_R)
        else:
          self.pwm.set_pwm(0, 0, servo_stop_R)
          self.pwm.set_pwm(1, 0, servo_stop_L)
        #self.get_logger().info(msg.data)

def main():
    try:
      rclpy.init()
      node = servo_control()
      rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


