#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("Node started!")
        self.counter = 0
        self.create_timer(0.5,self.timer_callback)
    
    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("Counter: "+ str(self.counter)) 

def main(args=None):
    rclpy.init(args=args)
    node = MyNode("opps_node")
    node1 = MyNode("second_node")
    rclpy.spin(node)
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__=="__main__":
    main()
