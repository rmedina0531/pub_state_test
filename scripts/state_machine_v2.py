#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
#from subscriber_state_machine import WaitForTwo
# define state Foo
from state_machine.approach_state import Approach
from state_machine.execute_task_state import Execute_Task
from state_machine.search_state import Search
from state_machine.tracker_state import Tracker


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
        smach.StateMachine.add('approach', Approach(),
                               transitions={'arrived':'execute'})
        smach.StateMachine.add('execute', Execute_Task(),
                               transitions={'complete':'track'})
        smach.StateMachine.add('track', Tracker(),
                               transitions={'unfinished':'search', 'finished':'completed'})

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()
