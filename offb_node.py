#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
import time
from geometry_msgs.msg import PoseStamped, Vector3
from nav_msgs.msg import Odometry
from mavros_msgs.msg import State
from mav_msgs.msg import Actuators
import time
odometry_msg = Odometry()
actuator_msg = Actuators()

def odometry_cb(msg):
    global odometry_msg
    odometry_msg = msg

if __name__ == '__main__':
    rospy.init_node('offb_node_py')
    motor_velocity_reference_pub = rospy.Publisher('/crazyflie2/command/motor_speed', Actuators, queue_size=1)
    rospy.Subscriber('/crazyflie2/odometry', Odometry, callback = odometry_cb)
    rate = rospy.Rate(100)
    time.sleep(5)
    
    speed = 2300
    while(1):
        Z = odometry_msg.pose.pose.position.z
        
        actuator_msg.angular_velocities = [speed,speed,speed,speed]
        actuator_msg.header.stamp = odometry_msg.header.stamp
        motor_velocity_reference_pub.publish(actuator_msg)
        print('Hello, !',odometry_msg)
        #print('Hello, !',actuator_msg)
        rate.sleep()
