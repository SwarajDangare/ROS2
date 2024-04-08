import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32

class Counter(Node):

    def __init__(self):
        super().__init__("number_counter")
        self.subscriptions_ = self.create_subscription(Int32,"number",self.callback,10)
        self.publishers_ = self.create_publisher(Int32, "number_counter",10)
        self.get_logger().info("Node Started!")
        self.counter_ = 0

    def callback(self,msg):
        self.counter_ += msg.data
        self.get_logger().info("Counter: " + str(self.counter_))
        new_msg = Int32()
        new_msg.data = self.counter_
        self.publishers_.publish(new_msg)

    

def main(args=None):
    rclpy.init(args=args)
    node = Counter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()