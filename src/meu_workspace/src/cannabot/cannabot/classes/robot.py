import rclpy
from geometry_msgs.msg import Twist, Vector3
# from turtlebot3_teleop import


class TurtleBot(rclpy.Node):
	def __init__(self):
		super().__init__('turtlebot')

		self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

	def move(self, linear: Vector3, angular: Vector3):
		msg = Twist()
		msg.linear = linear
		msg.angular = angular
		self.publisher_.publish(msg)

	def move_forward(self, speed: float):
		self.move(Vector3(x=speed), Vector3())

	def move_backward(self, speed: float):
		self.move(Vector3(x=-speed), Vector3())