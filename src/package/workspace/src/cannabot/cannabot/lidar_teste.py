#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class CollisionAvoidance:
    def __init__(self):
        rospy.init_node('collision_avoidance', anonymous=True)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.safe_distance = 0.5 # Defina a distância de segurança em metros

    def scan_callback(self, data):
        # Obtém os dados do Lidar
        ranges = data.ranges

        # Verifica se há obstáculos dentro da distância de segurança e enviar o indice da array

        if min(ranges) < self.safe_distance:
            # Se houver obstáculos próximos, pare o TurtleBot3

            print('Obstáculo detectado')
            print('Distância:', min(ranges))
            print('Índice:', ranges.index(min(ranges)))
            self.stop_robot()
        else:
            # Se não houver obstáculos próximos, continue em frente
            self.move_forward()


    def run(self):
        # Mantém o programa em execução
        rospy.spin()

if __name__ == '__main__':
    try:
        avoidance = CollisionAvoidance()
        avoidance.run()
    except rospy.ROSInterruptException:
        pass
