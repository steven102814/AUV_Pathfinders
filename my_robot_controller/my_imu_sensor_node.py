import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import rospy
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.sensor = LSM6DSOX(self.i2c)

    def timer_callback(self):
        accel_data = self.sensor.acceleration
        gyro_data = self.sensor.gyro
        sensor_msg = "Acceleration: X:{:.2f}, Y: {:.2f}, Z: {:.2f} m/s^2; Gyro X:{:.2f}, Y: {:.2f}, Z: {:.2f} radians/s".format(
            accel_data[0], accel_data[1], accel_data[2], gyro_data[0], gyro_data[1], gyro_data[2])
        self.publisher_.publish(String(data=sensor_msg))
        self.get_logger().info('Publishing: "%s"' % sensor_msg)

def main(args=None):
    rclpy.init(args=args)
    sensor_publisher = SensorPublisher()
    rclpy.spin(sensor_publisher)
    sensor_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
