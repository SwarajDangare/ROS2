import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
import random

class Number(Node):

    def __init__(self):
        super().__init__("number_publisher")
        self.publishers_ = self.create_publisher(Int32,"/number",10)
        self.get_logger().info("Node Started!")
        self.timer_ = self.create_timer(1,self.timer_callback)
    
    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(0, 10)
        self.get_logger().info("Random Number: " + str(msg.data))
        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Number()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()