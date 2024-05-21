from fastapi import FastAPI, WebSocket
import time
import json
import threading
from rclpy.node import Node
import rclpy
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import signal

# Inicializar o ROS 2 e criar o robô TurtleBot
robot = Robot()

def ws_app(robot):
    app = FastAPI()

    # Rota para receber comandos de movimento do robô
    @app.websocket("/ws_control")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                # Receber o comando de movimento do robô
                data = await websocket.receive_text()

                # Parse do JSON recebido
                message_data = json.loads(data)
                command = message_data['control'] # Comando de movimento
                # sent_time = float(message_data['timestamp']) # Timestamp de envio da mensagem

                # Calcular a latência da mensagem
                # current_time = time.time()
                # latency = current_time - sent_time  # Calcula a latência da mensagem

                # print(f"Msg recebida: {command} com {latency} s de latência")
                # await websocket.send_text(json.dumps({"latency": latency}))   

                # Atualizar o estado do robô
                robot.state = command

        except Exception as e:
            print(f"Erro: {e}")
            await websocket.close()

class Robot:
    def __init__(self):
        rclpy.init(args=None)
        self.node = rclpy.create_node('ros_turtlebot_teleop')

        self.publisher = self.node.create_publisher(Twist, '/cmd_vel', 10)
        self.node.create_subscription(Odometry, '/odom', self.odometry_callback, 10)
        self.node.create_service(Empty, '/emergency_stop_teleop', self.emergency_stop_external)
        self.reported_speed = Twist()

        self.state = 'stopped'
        self.ready = False
        self.thread = threading.Thread(target=self.await_ready_then_start)
        self.thread.start()

    def await_ready_then_start(self):
        self.node.get_logger().info('Aguardando o estado de prontidão do robô...')
        while not self.ready: 
            time.sleep(0.1)
        self.node.get_logger().info('Robô disponível! Iniciando teleoperação...')
        ws_app(robot)

    def emergency_stop_external(self, request, response):
        self.node.get_logger().info('Recebido pedido de parada de emergência externa')
        print('\n')
        self.node.get_logger().info('PARADA DE EMERGÊNCIA ATIVADA')
        signal.pthread_kill(self.thread.ident, signal.SIGUSR1)
        return response

    def timer_callback(self):
        twist = Twist()

        match self.state:
            case 'stopped':
                twist.linear.x = 0.0
                twist.angular.z = 0.0
            case 'forward':
                twist.linear.x = 0.5
                twist.angular.z = 0.0
            case 'left':
                twist.linear.x = 0.0
                twist.angular.z = 1.0
            case 'right':
                twist.linear.x = 0.0
                twist.angular.z = -1.0
            case 'backward':
                twist.linear.x = -0.5
                twist.angular.z = 0.0
            case _:
                self.node.get_logger().warn(f'Invalid state: {self.state}')

        self.publisher.publish(twist)

    def odometry_callback(self, msg):
        self.reported_speed = msg.twist.twist
        if not self.ready: 
            self.ready = True

    def emergency(self):
        print('\n')
        self.node.get_logger().info('PARADA DE EMERGÊNCIA ATIVADA')
        self.stop()

    def stop(self):
        self.publisher.publish(Twist())
        self.node.get_logger().info('Parando o robô...\n')
        self.node.destroy_node()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    robot = Robot()
    rclpy.spin(robot.node)
    robot.node.destroy_node()
    rclpy.shutdown()