#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
from std_msgs.msg import Int32
import time
import threading
from publishers.light_pub import Light_publisher

from pub_state_test.msg import cv_data


class Search(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found'])

        self.mutex = threading.Lock()
        self.object_found = rospy.Subscriber('cv_data', cv_data, self.callback)

        self.gate_found = False
        self.dice_found = False

        self.light_pub = Light_publisher()

    def callback(self, data):
        self.mutex.acquire()
        self.gate_found = data.gate
        self.dice_found = data.dice
        self.mutex.release()

    def execute(self, userdata):
        #if self.subscriber is None:
        #    self.subscriber = rospy.Subscriber('cv_data', Int32, self.callback)
        #wait for a maximum of 30 seconds
        #rospy.loginfo(str(userdata))

        self.light_pub.mode('search_state')

        #need to find a way to clear the queue after the flag has been tripped
        while True:
            out = out = 'Gate=' + str(self.gate_found) + ', ' + "Dice=" + str(self.dice_found)
            rospy.loginfo(out)

            self.mutex.acquire()
            if self.gate_found or self.dice_found:
                rospy.loginfo('I found an object')
                #ok we received 2\
                self.mutex.release()
                return 'found'

            self.mutex.release()

            time.sleep(.1)
            #still waiting
        #we didn't get 2 in the 30 sec
        return 'failed'

# class Search(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=['found'])
#
#         self.mutex = threading.Lock()
#         self.object_found = rospy.Subscriber('cv_data', Int32, self.callback)
#
#         self.object_found = False
#
#     def callback(self, data):
#         self.mutex.acquire()
#         if data.data == 1:
#             self.object_found = True
#         else:
#             self.object_found = False
#         self.mutex.release()
#
#     def execute(self, userdata):
#         #if self.subscriber is None:
#         #    self.subscriber = rospy.Subscriber('cv_data', Int32, self.callback)
#         #wait for a maximum of 30 seconds
#         #rospy.loginfo(str(userdata))
#
#         #need to find a way to clear the queue after the flag has been tripped
#         while True:
#             rospy.loginfo(self.object_found)
#
#             self.mutex.acquire()
#             if self.object_found:
#                 rospy.loginfo('I found an object')
#                 #ok we received 2\
#                 self.object_found = False
#                 self.mutex.release()
#                 self.object_found = False
#                 return 'found'
#
#             self.mutex.release()
#
#             time.sleep(.1)
#             #still waiting
#         #we didn't get 2 in the 30 sec
#         return 'failed'
#


class Search2(Search):
    def __init__(self):
        True

    def __str__(self):
        return super().dice_found


    def execute(self, userdata):
        output = super().execute()



