#! /usr/bin/env python
import rospy
from utilities.comms import Publisher

def publisher_custom_msg():
    rospy.init_node('cv_node')

    # pub=rospy.Publisher('cv_data', cv_data, queue_size=1)
    pub = Publisher('cv_data', 'cv_data')

    rate=rospy.Rate(10)

    gate=False
    dice=False

    time=0

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
        # msg.gate = gate
        # msg.dice = dice
        rospy.loginfo(out)
        pub.publish(gate=gate, dice=dice)
        # pub.publish(msg)
        rate.sleep()

if __name__=='__main__':
    # publisher_count()
    publisher_custom_msg()

