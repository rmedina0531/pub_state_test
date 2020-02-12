#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
from std_msgs.msg import Int32
import time
import threading

class Execute_Task(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['complete'])

    def execute(self, userdata):
        # wait for a maximum of 30 seconds
        # rospy.loginfo(str(userdata))
        count = 0
        while True:
            # simulate arrival procedure
            if count == 100:
                # ok we received 2
                return 'complete'
            count += 1
            time.sleep(.1)



