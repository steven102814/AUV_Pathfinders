# #!/usr/bin/env python3
# from std_msgs.msg import String
# import rclpy
# from rclpy.node import Node

# class MyDVL(Node):
#     def __init__(self):
#         super().__init__("my_dvl")
#         self.counter_ = 0
#         self.publisher_ = self.create_publisher(String, 'my_dvl_data', 10)
#         self.create_timer(1.0, self.timer_callback)

#     def timer_callback(self):
#         msg = String()
#         msg.data = f"Hello {self.counter_}"
#         self.publisher_.publish(msg)
#         self.get_logger().info(f"Publishing: {msg.data}")
#         self.counter_ += 1

# class MyJetsonOrin(Node):
#     def __init__(self):
#         super().__init__("my_jetson_orin")
#         self.subscription = self.create_subscription(
#             String,
#             'my_dvl_data',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning

#     def listener_callback(self, msg):
#         self.get_logger().info(f"I heard: {msg.data}")

# def main(args=None): 
#     rclpy.init(args=args) 

#     my_dvl_node = MyDVL()
#     my_jetson_orin_node = MyJetsonOrin()

#     executor = rclpy.executors.MultiThreadedExecutor()
#     executor.add_node(my_dvl_node)
#     executor.add_node(my_jetson_orin_node)

#     try:
#         executor.spin()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         executor.shutdown()
#         rclpy.shutdown() 

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3
from std_msgs.msg import String
import rclpy
from rclpy.node import Node

class MyDVL(Node):
    def __init__(self):
        super().__init__("my_dvl")
        self.counter_ = 0
        self.publisher_ = self.create_publisher(String, 'my_dvl_data', 10)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"DVL Data {self.counter_}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.counter_ += 1

class ZedCamera(Node):
    def __init__(self):
        super().__init__("zed_camera")
        self.counter_ = 0
        self.publisher_ = self.create_publisher(String, 'zed_camera_data', 10)
        self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"Zed Camera Data {self.counter_}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.counter_ += 1

class MyJetsonOrin(Node):
    def __init__(self):
        super().__init__("my_jetson_orin")
        self.my_dvl_subscription = self.create_subscription(
            String,
            'my_dvl_data',
            self.my_dvl_listener_callback,
            10)
        self.zed_camera_subscription = self.create_subscription(
            String,
            'zed_camera_data',
            self.zed_camera_listener_callback,
            10)

    def my_dvl_listener_callback(self, msg):
        self.get_logger().info(f"I heard on DVL: {msg.data}")

    def zed_camera_listener_callback(self, msg):
        self.get_logger().info(f"I heard on Zed Camera: {msg.data}")

def main(args=None): 
    rclpy.init(args=args) 

    my_dvl_node = MyDVL()
    zed_camera_node = ZedCamera()
    my_jetson_orin_node = MyJetsonOrin()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(my_dvl_node)
    executor.add_node(zed_camera_node)
    executor.add_node(my_jetson_orin_node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        rclpy.shutdown() 

if __name__ == '__main__':
    main()
