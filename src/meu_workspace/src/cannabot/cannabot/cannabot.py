import typer
import rclpy
from rclpy.node import Node
from InquirerPy.resolver import prompt
from InquirerPy.utils import InquirerPyKeybindings
from geometry_msgs.msg import Twist, Vector3
import time

# from classes.robot import TurtleBot

app = typer.Typer()

def custom_input(prompt):
    """Custom input function that checks for 'Q' and raises an exception."""
    try:
        user_input = input(prompt)
        print(user_input)
        if user_input.upper() == 'Q':
            raise KeyboardInterrupt  # Simulate KeyboardInterrupt on 'Q' press
        return user_input
    except EOFError:
        return ''  # Handle EOFError if needed

def show_menu():
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': ['front', 'back', 'left', 'right', 'exit', 'stop'],
        },
    ]

    keybindings: InquirerPyKeybindings = {
        "interrupt": [{"key": "q"}, {"key": "c-c"}],
    }

    try:
        return prompt(questions, keybindings=keybindings)['action']
    except KeyboardInterrupt:
        return 'panic'

def main():
    rclpy.init(args=None)
    robot = TurtleBot()

    print(
"""
Se em qualquer momento você desejar parar o robô, pressione 'Q'.
"""
    )
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
            case 'stop':
                print("Parada de emergência")
                robot.emergency_stop()
            case 'panic':
                print("Parada de emergência")
                robot.emergency_stop()
                robot.destroy_node()
                rclpy.shutdown()
                exit()
            case 'exit':
                robot.destroy_node()
                rclpy.shutdown()
                exit()

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

    # Seta todas as velocidades para 0 para parar o robô imediatamente
    def emergency_stop(self):
        self.move(Vector3(x=0.0, y=0.0, z=0.0), Vector3(), 0.0)