import inquirer
import typer
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import String
import time

# from classes.robot import TurtleBot

app = typer.Typer()

def show_menu():
    questions = [
        inquirer.List('action', message="What do you want to do?", choices=[
            'front', 'back', 'left', 'right', 'exit'
        ])
    ]
    return inquirer.prompt(questions)['action']


def main():
    rclpy.init(args=None)
    robot = TurtleBot()
    while True:
        action = show_menu()
        match action:
            case 'front':
                print("Mover para frente")
                robot.move_forward(0.1, 1.0)
            case 'back':
                print("Mover para trás")
                robot.move_backward(0.1, 1.0)
            case 'left':
                print("Mover para a esquerda")
                robot.rotate_left(2.0, 1.0)
            case 'right':
                print("Mover para a direita")
                robot.rotate_right(2.0, 1.0)
            case 'exit':
                print("Exit")
                break

    # while True:
    # if keyboard.is_pressed('w'):
    #     robot.move_forward(speed)
    # elif keyboard.is_pressed('s'):
    #     robot.move_backward(speed)
    # elif keyboard.is_pressed('a'):
    #     robot.rotate_left(speed)
    # elif keyboard.is_pressed('d'):
    #     robot.rotate_right(speed)
    # elif keyboard.is_pressed('esc'):
    #     break  # Exit on pressing 'esc'
    # else:
    #     robot.stop()  # Stop if no key is pressed
    # rclpy.spin_once(robot, timeout_sec=0.1)

    robot.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


class TurtleBot(Node):
    def __init__(self):
        super().__init__('turtlebot')

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    # Função para enviar comandos de movimento para o robô
    def move(self, linear: Vector3, angular: Vector3, duration: float):
        msg = Twist()
        msg.linear = linear
        msg.angular = angular
        self.publisher_.publish(msg)

        # Esperar o tempo de duração antes de para o movimento
        time.sleep(duration)  # Simples delay para esperar antes de parar o movimento
        self.stop()
    
    # 
    def stop(self):
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)

    def move_forward(self, speed: float, duration: float):
        # Criar um Vector3 com a velocidade linear
        self.move(Vector3(x=speed, y=0.0, z=0.0), Vector3(), duration)

    def move_backward(self, speed: float, duration: float):
        self.move(Vector3(x=-speed, y=0.0, z=0.0), Vector3(), duration)

    def rotate_left(self, speed: float, duration: float):
        # Criar um Vector3 com a velocidade angular
        self.move(Vector3(), Vector3(z=speed), duration)

    def rotate_right(self, speed: float, duration: float):
        self.move(Vector3(), Vector3(z=-speed), duration)