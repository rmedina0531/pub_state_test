#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import time
from utilities.comms import Subscriber, Publisher
class Search(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found'])
        self.sub = Subscriber('cv_data', 'cv_data')
        self.pub = Publisher('lights_data', 'lights_data')

    def execute(self, userdata):
        self.pub.publish('search_state')
        while True:
            object_data = self.sub.get_data()
            out = 'Gate=' + str(object_data.gate) + ', ' + "Dice=" + str(object_data.dice)
            rospy.loginfo(out)

            if object_data.gate or object_data.dice:
                rospy.loginfo('I found an object')
                return 'found'

            time.sleep(.1)

        return 'failed'
