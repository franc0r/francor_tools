import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped

class UpdateStampNode(Node):

  def __init__(self):
    super().__init__('map_repub_node')
    self.publisher_ = self.create_publisher(PoseStamped, '/local_goal_pose', 10)

    self.subscription = self.create_subscription(PoseStamped, '/goal_pose',  self.listener_callback, 10)

  def listener_callback(self, msg: PoseStamped):
    self.get_logger().info('I heard: "%s"' % msg.header.stamp)
    #update stamp
    msg.header.stamp = self.get_clock().now().to_msg()
    self.get_logger().info('new stamp: "%s"' % msg.header.stamp)
    self.publisher_.publish(msg)





def main(args=None):
  rclpy.init(args=args)

  update_stamp_node = UpdateStampNode()

  try:
    rclpy.spin(update_stamp_node)
  except KeyboardInterrupt:
    pass

  update_stamp_node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()