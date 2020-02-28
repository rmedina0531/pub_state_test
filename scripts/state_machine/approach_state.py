#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import time
import threading

class Approach(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['arrived'])

    def execute(self, userdata):
        #wait for a maximum of 30 seconds
        #rospy.loginfo(str(userdata))
        count = 0
        while True:
            #simulate arrival procedure
            if count == 100:
                #ok we received 2
                return 'arrived'
            count+=1
            time.sleep(.1)