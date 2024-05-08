import inquirer
import typer
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Robot(Node):
    def __init__(self):
        super().__init__('robot')
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/turtle1/cmd_vel',
            qos_profile=10
        )
        timer_period = 0.5
        self.timer = self.create_timer(
            timer_period_sec=timer_period, 
            callback=self.timer_callback
            )
        
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.5
        self.publisher.publish(msg)
        # self.get_logger().info("Publicando mensagem de movimento")

app = typer.Typer()

def moviment_publisher():
    pass

def front():
    print("Move to the front of the line")

def back():
    print("Move to the back of the line")

def left():
    graus_left = inquirer.text("Quantos graus para esquerda deseja virar?")
    print(f"Move to the left in {graus_left} degrees")

def right():
    graus_right = inquirer.text("Quantos graus para direita deseja virar?")
    print(f"Move to the right in {graus_right} degrees")

def show_menu():
    questions = [inquirer.List('action', message="What do you want to do?", choices=['front', 'back', 'left', 'right', 'exit'])]
    answers = inquirer.prompt(questions)
    return answers['action']

def init_robot(args=None):
    print("Init robot")
    # rclpy.init(args=args)
    # robot = Robot()
    # rclpy.spin(robot)
    # robot.destroy_node()
    # rclpy.shutdown()

def main():
    init_robot()

    while True:
        action = show_menu()
        if action == 'front':
            front()
        elif action == 'back':
            back()
        elif action == 'left':
            left()
        elif action == 'right':
            right()
        elif action == 'exit':
            break

if __name__ == "__main__":
    main()
