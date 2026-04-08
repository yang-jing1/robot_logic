import rclpy
from rclpy.node import Node
from coord_interfaces.msg import CoordTask

class ExecutorNode(Node):
    def __init__(self):
        super().__init__('executor_node')
        self.sub = self.create_subscription(CoordTask, '/robot_b/mission_goal', self.callback, 10)
        self.get_logger().info('任务四：Robot B 执行节点已就绪！')

    def callback(self, msg):
        p = msg.map_point
        self.get_logger().info(f'[Robot B] 收到指令: {msg.action} | 目标: ({p.x:.2f}, {p.y:.2f}, {p.z:.2f})')

def main():
    rclpy.init()
    rclpy.spin(ExecutorNode())
    rclpy.shutdown()
