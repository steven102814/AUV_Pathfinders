#!/usr/bin/env python3
from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

#below intializes the node using OOP
class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        #self.get_logger().info("ROS")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " +str(self.counter_))
        self.counter_ += 1



def main(args=None): 
    rclpy.init(args=args) #start ros communications 

    #create the node in here for the program. inherited from class 
    node = MyNode()

    rclpy.spin(node) #node will continue to run until killed using control c 



    rclpy.shutdown() #shutdown ros communications 



if __name__ == '__main__':
    main()