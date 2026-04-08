import rclpy
from rclpy.node import Node
from coord_interfaces.msg import RawDetection
from geometry_msgs.msg import Point

class DetectorNode(Node):
    def __init__(self):
        super().__init__('detector_node')
        # 任务要求：通过参数设置坐标 (x,y,z)，默认设为 0.5
        self.declare_parameter('x', 0.5)
        self.declare_parameter('y', 0.0)
        self.declare_parameter('z', 0.1)
        
        self.pub = self.create_publisher(RawDetection, '/robot_a/raw_detection', 10)
        # 任务要求：10Hz 频率 (0.1秒一次)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('任务二：YOLO 模拟节点已启动')

    def timer_callback(self):
        msg = RawDetection()
        msg.robot_name = "Robot_A"
        msg.point.x = self.get_parameter('x').value
        msg.point.y = self.get_parameter('y').value
        msg.point.z = self.get_parameter('z').value
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(DetectorNode())
    rclpy.shutdown()
