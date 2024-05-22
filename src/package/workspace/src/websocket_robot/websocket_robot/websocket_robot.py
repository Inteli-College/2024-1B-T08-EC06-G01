from fastapi import FastAPI, WebSocket
import time
import json
import threading
import uvicorn
from rclpy.node import Node
import rclpy
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import signal

class Robot(Node):
    def __init__(self):
        super().__init__('ros_turtlebot_teleop')

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.create_subscription(Odometry, '/odom', self.odometry_callback, 10)
        self.create_service(Empty, '/emergency_stop_teleop', self.emergency_stop_external)
        self.reported_speed = Twist()

        self.state = 'stopped'
        self.ready = False

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Aguardando o estado de prontidão do robô...')

    def emergency_stop_external(self, request, response):
        self.get_logger().info('Recebido pedido de parada de emergência externa')
        self.get_logger().info('PARADA DE EMERGÊNCIA ATIVADA')
        self.stop()
        return response

    def timer_callback(self):
        twist = Twist()

        if self.state == 'stopped':
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        elif self.state == 'forward':
            twist.linear.x = 0.5
            twist.angular.z = 0.0
        elif self.state == 'left':
            twist.linear.x = 0.0
            twist.angular.z = 1.0
        elif self.state == 'right':
            twist.linear.x = 0.0
            twist.angular.z = -1.0
        elif self.state == 'backward':
            twist.linear.x = -0.5
            twist.angular.z = 0.0
        else:
            self.get_logger().warn(f'Invalid state: {self.state}')

        self.publisher.publish(twist)

    def odometry_callback(self, msg):
        self.reported_speed = msg.twist.twist
        if not self.ready:
            self.ready = True
            self.get_logger().info('Robô disponível! Iniciando teleoperação...')

    def emergency(self):
        self.get_logger().info('PARADA DE EMERGÊNCIA ATIVADA')
        self.stop()

    def stop(self):
        self.publisher.publish(Twist())
        self.get_logger().info('Parando o robô...')
        rclpy.shutdown()

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

                print(f"Recebido: {data}")

                # Parse do JSON recebido
                message_data = json.loads(data)
                command = message_data['control']  # Comando de movimento
                print(f"Comando: {command}")
                # Atualizar o estado do robô
                robot.state = command

        except Exception as e:
            print(f"Erro: {e}")
            await websocket.close()

    return app

def main(args=None):
    rclpy.init(args=args)
    robot = Robot()

    # Iniciar o servidor WebSocket em uma thread separada
    ws_thread = threading.Thread(target=lambda: uvicorn.run(ws_app(robot), host="0.0.0.0", port=3000))
    ws_thread.start()

    rclpy.spin(robot)
    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
