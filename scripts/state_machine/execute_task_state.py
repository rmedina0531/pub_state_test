#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import time
import threading
from utilities.comms import Publisher

class Execute_Task(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['complete'])
        self.pub = Publisher('light_data', 'light_data')

    def execute(self, userdata):
        # wait for a maximum of 30 seconds
        # rospy.loginfo(str(userdata))
        self.pub.publish('execute_state')
        count = 0
        while True:
            # simulate arrival procedure
            if count == 100:
                # ok we received 2
                return 'complete'
            count += 1
            time.sleep(.1)



