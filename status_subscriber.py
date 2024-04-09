import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from om_aiv_msg.msg import Status
import time

class StatusSubscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber')
        self.subscription_status = self.create_subscription(
            Status, '/ldarcl_status', self.status_callback, 10)
        self.subscription_status  # prevent unused variable warning
        self.battery = -1
        self.robot_x = None
        self.robot_y = None
        self.robot_theta = None
        self.status_received = False
        self.status_msg = None
        

    def status_callback(self, msg):
        if not self.status_received:
            self.robot_x = msg.location.x / 1000
            self.robot_y = msg.location.y / 1000
            self.robot_theta = msg.location.theta
            self.status_received = True
            self.battery = msg.state_of_charge
            self.send_status()

    def send_status(self):
        self.status_msg = f"{self.robot_x}, {self.robot_y}, {self.robot_theta}, {self.battery}"
        print(f"{self.robot_x}, {self.robot_y}, {self.robot_theta}, {self.battery}")
        return f"{self.robot_x}, {self.robot_y}, {self.robot_theta}, {self.battery}"

def main(args=None):
    rclpy.init(args=args)
    status_subscriber = StatusSubscriber()

    while rclpy.ok() and not (status_subscriber.status_received):
        rclpy.spin_once(status_subscriber)
    
    
    status_subscriber.get_logger().info('Exiting gracefully...')
    rclpy.shutdown()

    if status_subscriber.status_msg:
        return status_subscriber.status_msg

if __name__ == '__main__':
    main()
