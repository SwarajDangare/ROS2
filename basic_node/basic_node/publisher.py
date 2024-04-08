#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MyPublisher(Node):

    def __init__(self):
        super().__init__("publisher_node")
        self.publishers_ = self.create_publisher(String,"/dummy_topic",10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info("publisher node started")
        self.counter_ = 0

    def timer_callback(self):
        self.counter_ += 1
        msg = String()
        msg.data = "Counter: " + str(self.counter_)
        self.get_logger().info(msg.data)
        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
