import inquirer
import typer
import rclpy
from classes.robot import TurtleBot

app = typer.Typer()

def show_menu():
    return inquirer.prompt(
        inquirer.List('action', message="What do you want to do?", choices=[
            'front', 'back', 'left', 'right', 'exit'
        ]
    ))['action'] # type: ignore


def main():
    rclpy.init(args=None)
    robot = TurtleBot()
    while True:
        action = show_menu()
        match action:
            case 'front':
                robot.move_forward(0.1)
            case 'back':
                robot.move_backward(0.1)
            case 'left':
                robot.rotate_left(0.1)
            case 'right':
                robot.rotate_right(0.1)
            case 'exit':
                break

    robot.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
