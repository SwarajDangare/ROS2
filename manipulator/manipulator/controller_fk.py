import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from rclpy.clock import Clock
import sys

class TrajectoryPublisher(Node):
    
    def __init__(self):
        super().__init__('trajectory_node')
        topic_ = "/joint_states"
        self.joints = ['base_arm1_joint', 'arm1_arm2_joint', 'arm2_arm3_joint']
        # self.goal_ =[0.0, 0.0, 0.0]
        self.goal_= [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
        self.publisher_ = self.create_publisher(JointState, topic_, 10)
        self.timer_ = self.create_timer(0.1,self.timer_callback)

        
        
    def timer_callback(self):
        msg = JointState()
        current_time = Clock().now().to_msg()
        msg.header.stamp.sec = current_time.sec
        msg.header.stamp.nanosec = current_time.nanosec
        msg.name = self.joints
        msg.position = self.goal_
        self.publisher_.publish(msg)
        self.get_logger().info("Reached the position...")
        exit()
        
def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()