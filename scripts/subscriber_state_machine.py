#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
from std_msgs.msg import Int32
import time
import threading

class WaitForTwo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'failed'])

        self.mutex = threading.Lock()
        self.two_received = False

        self.subscriber = rospy.Subscriber('count', Int32, self.callback)

    def callback(self, data):
        self.mutex.acquire()
        if data.data == 30:
            self.two_received = True
        self.mutex.release()

    def execute(self, userdata):
        #wait for a maximum of 30 seconds 
        rospy.loginfo(str(userdata))
        while True:
            self.mutex.acquire()
            if self.two_received:
                #ok we received 2
                return 'success'

            self.mutex.release()

            time.sleep(.1)
            #still waiting
        #we didn't get 2 in the 30 sec
        return 'failed'



