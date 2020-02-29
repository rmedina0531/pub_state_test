#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import time
import threading
from utilities.comms import Publisher


class Step1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['complete'])
        self.pub = Publisher('light_data', 'light_data')

    def execute(self, userdata):
        self.pub.publish('approach_state')
        count = 0

        while True:
            if count == 50:
                return 'complete'
            count += 1
            time.sleep(.1)

class Step2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['complete'])

    def execute(self, userdata):
        count = 0

        while True:
            if count == 50:
                return 'complete'
            count += 1
            time.sleep(.1)

# class Approach(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=['arrived'])
#
#     def execute(self, userdata):
#         #wait for a maximum of 30 seconds
#         #rospy.loginfo(str(userdata))
#         count = 0
#         while True:
#             #simulate arrival procedure
#             if count == 100:
#                 #ok we received 2
#                 return 'arrived'
#             count+=1
#             time.sleep(.1)
#
# def approach_state_machine():
#     s_machine = smach.State(outcomes=['arrived'])
#
#     with s_machine:
#
#         smach.StateMachine.add('Step1', Step1(), transitions={'complete':'Step2'})
#         smach.StateMachine.add('Step2', Step2(), transitions={'complete':'arrived'})
#
#     smach.StateMachine.add('approach', s_machine,
#                                transitions={'arrived': 'execute'})

def add_states():
    smach.StateMachine.add('Step1', Step1(), transitions={'complete': 'Step2'})
    smach.StateMachine.add('Step2', Step2(), transitions={'complete': 'arrived'})