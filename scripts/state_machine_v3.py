#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
#from subscriber_state_machine import WaitForTwo
# define state Foo
from state_machine.execute_task_state import Execute_Task
from state_machine.search_state import Search
from state_machine.tracker_state import Tracker
from state_machine.approach_state_v2 import add_states

def main():
    rospy.init_node('sub_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['completed'])

    # Open the container
    with sm:
        # Add states to the container
        # note these states can be defined as their own state machine with its own set of in and outs
        # look up syntax on the tutorials
        # look up way to pass the data between states
            #need to pass the data on which object was detected to the approach, execute and tracking states

        smach.StateMachine.add('search', Search(),
                              transitions={'found':'approach'})

        approach_state = smach.StateMachine(outcomes=['arrived'])
        with approach_state:
            add_states()
        smach.StateMachine.add('approach', approach_state, transitions={'arrived':'execute'})

        smach.StateMachine.add('execute', Execute_Task(),
                               transitions={'complete':'track'})
        smach.StateMachine.add('track', Tracker(),
                               transitions={'unfinished':'search', 'finished':'completed'})




    #set up the introspective server for a state machine

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()
