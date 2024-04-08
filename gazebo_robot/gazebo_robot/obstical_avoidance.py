#!/usr/bin/env python3
import rclpy
import rclpy.node as node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObsticalAvoidance(node.Node):
    def __init__(self):
        super().__init__("obstical_avoidance")
        self.get_logger().info("Obstical Avoidance started......")
        self.get_logger().info("NO Object detected!!!, moving forward...")
        self.obj_pub = self.create_publisher(Twist,"/cmd_vel",10)
        self.obj_sub = self.create_subscription(LaserScan,"/gazebo_lidar/out",self.cmd_vel,10)
    
    #if object is detected then go back and turn
    def cmd_vel(self, laser):
        twist_msg = Twist()
        for laser in laser.ranges:
            if laser < 1.25:
                twist_msg.linear.x = 0.0
                twist_msg.angular.z = -3.14/2
                self.get_logger().warn("Object detected!!!, turning...")
                break
            else:
                twist_msg.linear.x = 0.5
                twist_msg.angular.z = 0.0
        self.obj_pub.publish(twist_msg)
        
def main(args = None):
    rclpy.init(args = args)
    node = ObsticalAvoidance()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()  