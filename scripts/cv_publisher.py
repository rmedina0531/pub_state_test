#! /usr/bin/env python
import rospy
from pub_state_test.msg import cv_data

#add in functionality to send confirmation of various objects
    #to do later

from std_msgs.msg import Int32

def publisher_count():
    rospy.init_node('cv_node')

    pub=rospy.Publisher('cv_data', Int32, queue_size=1)

    rate=rospy.Rate(10)

    time = 0;
    value = 0;
    while True:
        time += 1
        if time > 50:
            value = 1
        if time > 60:
            value = 0
        if time > 380:
            value = 1
        rospy.loginfo(value)
        pub.publish(value)

        rate.sleep()

def publisher_custom_msg():
    rospy.init_node('cv_node')

    pub=rospy.Publisher('cv_data', cv_data, queue_size=1)

    rate=rospy.Rate(10)

    gate=False
    dice=False

    time=0
    msg = cv_data()

    while True:
        time += 1
        if time > 50:
            gate=True
        if time > 60:
            gate=False
        if time > 380:
            dice = True
        if time > 390:
            dice = False
        if time > 450:
            break

        out = 'Gate=' + str(gate) + ', ' + "Dice=" + str(dice)
        msg.gate = gate
        msg.dice = dice
        rospy.loginfo(out)
        pub.publish(msg)
        pub.publish(msg)

        rate.sleep()

if __name__=='__main__':
    # publisher_count()
    publisher_custom_msg()

