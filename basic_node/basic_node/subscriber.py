#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MySubscriber(Node):

    def __init__(self):
        super().__init__("subscriber")
        self.subscriptions_ = self.create_subscription(String, "dummy_topic",self.callback,10)
        self.get_logger().info("subscriber node started")
    
    def callback(self,msg):
        self.get_logger().info("Subscribing: " + msg.data)
    

def main(args=None):
    rclpy.init(args=args)
    node = MySubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()