import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from om_aiv_msg.msg import Status
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from scipy.ndimage import gaussian_filter
import base64
import io

class LaserSubscriber(Node):
    def __init__(self, radius=1.5):
        super().__init__('laser_subscriber')
        self.subscription_laser = self.create_subscription(
            String, '/ldarcl_laser', self.laser_callback, 10)
        self.subscription_status = self.create_subscription(
            Status, '/ldarcl_status', self.status_callback, 10)
        self.subscription_laser  # prevent unused variable warning
        self.subscription_status  # prevent unused variable warning
        self.x_values = []
        self.y_values = []
        self.robot_x = None
        self.robot_y = None
        self.robot_theta = None
        self.laser_received = False
        self.status_received = False
        self.plot_ready = False
        self.radius = radius  # Radius of the circle in meters

    def laser_callback(self, msg):
        if not self.laser_received:
        # Split the string into individual values
            msgT = msg.data[8:]
            data_values = msgT.split()
            # Extract x and y coordinates and convert to meters
            self.x_values = [int(data_values[i]) / 1000 for i in range(0, len(data_values), 2)]
            self.y_values = [int(data_values[i+1]) / 1000 for i in range(0, len(data_values), 2)]
            self.laser_received = True
            self.check_and_plot_data()

    def status_callback(self, msg):
        if not self.status_received:
            self.robot_x = msg.location.x / 1000
            self.robot_y = msg.location.y / 1000
            self.robot_theta = msg.location.theta
            self.status_received = True
            self.check_and_plot_data()

    def check_and_plot_data(self):
        if self.laser_received and self.status_received and not self.plot_ready:
            self.plot_ready = True
            self.plot_data_if_ready()

    def plot_data_if_ready(self):
        if self.laser_received and self.status_received and self.plot_ready:
            # Convert lists to NumPy arrays
            self.x_values = np.array(self.x_values)
            self.y_values = np.array(self.y_values)

            # Plot the x, y coordinates as smaller and sharper grey circles
            plt.figure(figsize=(10, 8))
            for x, y in zip(self.x_values, self.y_values):
                circle = Circle((x, y), 0.05, color='grey', alpha=1, edgecolor='black')
                plt.gca().add_patch(circle)

            # Plot the robot position as an arrow in orange color
            arrow_length = 0.5  # adjust this value to change the arrow length
            plt.arrow(self.robot_x, self.robot_y,
                    arrow_length * np.cos(np.radians(self.robot_theta)),
                    arrow_length * np.sin(np.radians(self.robot_theta)),
                    head_width=0.15, head_length=0.3, fc='orange', ec='orange', linewidth=2)

            # Create a circle around the robot position with outer thickness
            outer_circle = Circle((self.robot_x, self.robot_y), self.radius + 0.1, color='black', fill=False, linewidth=2)
            plt.gca().add_patch(outer_circle)

            # Create a circle around the robot position with actual radius
            inner_circle = Circle((self.robot_x, self.robot_y), self.radius, color='black', fill=False, linewidth=2)
            plt.gca().add_patch(inner_circle)

            # Blur the points outside the circle
            mask = np.sqrt((self.x_values - self.robot_x)**2 + (self.y_values - self.robot_y)**2) > self.radius
            blurred_x_values = gaussian_filter(self.x_values[mask], sigma=2)
            blurred_y_values = gaussian_filter(self.y_values[mask], sigma=2)
            plt.plot(blurred_x_values, blurred_y_values, 'o', color='grey', alpha=0.5, markersize=3)

            # Add labels for the origin, robot position, and laser data
            plt.text(0, 0, 'Origin', fontsize=10, ha='right', va='bottom')
            plt.text(self.robot_x, self.robot_y, 'Robot Position', fontsize=10, ha='right', va='bottom')
            plt.text(np.mean(self.x_values), np.mean(self.y_values), 'Laser Data', fontsize=10, ha='right', va='bottom')

            plt.xlabel('X (m)', ha='right')
            plt.ylabel('Y (m)', va='top')
            plt.title('Robot Position and Laser Data')
            plt.grid(True)

            # Set origin to bottom right corner and flip the x-axis and y-axis
            plt.gca().set_aspect('equal', adjustable='box')
            plt.gca().invert_xaxis()
            plt.gca().invert_yaxis()

            # Move x-axis and y-axis ticks and labels to the same side
            plt.gca().tick_params(axis='x', direction='inout', labelrotation=0, pad=10, labeltop=True, labelbottom=False)
            plt.gca().tick_params(axis='y', direction='inout', pad=10, labelright=True, labelleft=False)

            # Display the plot
            # plt.show()

            # Convert plot to base64 and return
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
            buffer.seek(0)
            plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            buffer.close()

            plt.close()  # Close the plot to prevent it from being displayed
            # print(plot_base64)
            self.bstring = plot_base64
            return plot_base64  # Return the base64 string


def main(args=None, radius=2):  # Default radius value
    rclpy.init(args=args)
    laser_subscriber = LaserSubscriber(radius=radius)

    while rclpy.ok() and not (laser_subscriber.laser_received and laser_subscriber.status_received and laser_subscriber.plot_ready):
        rclpy.spin_once(laser_subscriber)

    laser_subscriber.get_logger().info('Exiting gracefully...')
    rclpy.shutdown()

    if laser_subscriber.bstring:
        return laser_subscriber.bstring

if __name__ == '__main__':
    import sys
    radius = float(sys.argv[1]) if len(sys.argv) > 1 else 2  # Accept radius from command line
    main(radius=radius)
