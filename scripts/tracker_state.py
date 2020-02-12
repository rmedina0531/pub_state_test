#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
from std_msgs.msg import Int32
import time
import threading

class Tracker(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['unfinished', 'finished'])
        self.completed = 0

    def execute(self, userdata):
        #wait for a maximum of 30 seconds
        #rospy.loginfo(str(userdata))
        self.completed += 1
        if self.completed == 2:
            return 'finished'
        else:
            return 'unfinished'
