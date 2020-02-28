#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import time
from utilities.comms import Subscriber

class Search(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found'])
        self.sub = Subscriber('cv_data', 'cv_data')
        # self.sub = CV_subscriber()

    def execute(self, userdata):
        #if self.subscriber is None:
        #    self.subscriber = rospy.Subscriber('cv_data', Int32, self.callback)
        #wait for a maximum of 30 seconds
        #rospy.loginfo(str(userdata))


        #need to find a way to clear the queue after the flag has been tripped
        while True:
            object_data = self.sub.get_data()
            out = 'Gate=' + str(object_data.gate) + ', ' + "Dice=" + str(object_data.dice)
            rospy.loginfo(out)

            if object_data.gate or object_data.dice:
                rospy.loginfo('I found an object')
                #ok we received 2\
                return 'found'

            time.sleep(.1)
            #still waiting
        #we didn't get 2 in the 30 sec
        return 'failed'
