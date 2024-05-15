#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data, QoSProfile
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class CollisionAvoidance(Node):
    def __init__(self):
        super().__init__('collision_avoidance')

        qos = QoSProfile(depth=10)
        self.scan_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            qos_profile=qos_profile_sensor_data
        )

        self.safe_distance = 0.5 # Defina a distância de segurança em metros

    def scan_callback(self, data):
        # Obtém os dados do Lidar
        ranges = data.ranges

        # Verifica se há obstáculos dentro da distância de segurança e enviar o índice da array
        if min(ranges) < self.safe_distance:
            # Se houver obstáculos próximos, pare o TurtleBot3
            print('Obstáculo detectado')
            print('Distância:', min(ranges))
            print('Índice:', ranges.index(min(ranges)))
        else:
            # Se não houver obstáculos próximos, continue em frente
            print('Nenhum obstáculo detectado')
            pass

def main(args=None):
    print('Starting scan listener')
    rclpy.init(args=args)
    avoidance = CollisionAvoidance()
    rclpy.spin(avoidance)
    rclpy.shutdown()
    print('done.')

if __name__ == '__main__':
    main()
