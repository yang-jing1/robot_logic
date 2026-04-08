import rclpy
from rclpy.node import Node
from coord_interfaces.msg import RawDetection, CoordTask
from coord_interfaces.srv import GetStatus

class CenterNode(Node):
    def __init__(self):
        super().__init__('center_node')
        self.sub = self.create_subscription(RawDetection, '/robot_a/raw_detection', self.callback, 10)
        self.pub = self.create_publisher(CoordTask, '/robot_b/mission_goal', 10)
        # 增加 Service 服务端
        self.srv = self.create_service(GetStatus, 'get_status', self.get_status_callback)
        self.get_logger().info('任务三：指挥中心解算节点及服务已启动')

    def callback(self, msg):
        task = CoordTask()
        task.map_point.x = msg.point.x + 1.0
        task.map_point.y = msg.point.y
        task.map_point.z = msg.point.z + 0.5
        task.action = "Wait" if task.map_point.x > 2.0 else "Catch"
        self.pub.publish(task)

    def get_status_callback(self, request, response):
        response.status = "Ready"  # 响应验收标准的 "Ready"
        self.get_logger().info('收到状态查询，回复: Ready')
        return response

def main():
    rclpy.init()
    rclpy.spin(CenterNode())
    rclpy.shutdown()
