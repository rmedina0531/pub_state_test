#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros


# define state Foo
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['outcome1', 'outcome2'],
                             input_keys=['first_in', 'second_in'],
                             output_keys=['first_out', 'second_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        userdata.second_out = [99,99,99,99]
        if userdata.first_in < 3:
            userdata.first_out = userdata.first_in + 1
            return 'outcome1'
        else:
            return 'outcome2'


# define state Bar
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['outcome1'],
                             input_keys=['first_in', 'second_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        rospy.loginfo('Counter = %f' % userdata.first_in)
        rospy.loginfo('Counter =' + str(userdata.second_in))
        return 'outcome1'


def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4'])
    sm.userdata.sm_counter_1 = 0
    sm.userdata.sm_counter_2 = [0,1,2,3]

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('FOO', Foo(),
                               transitions={'outcome1': 'BAR',
                                            'outcome2': 'outcome4'},
                               remapping={'first_in': 'sm_counter_1',
                                          'second_in': 'sm_counter_2',
                                          'first_out': 'sm_counter_1',
                                          'second_out': 'sm_counter_2'})
        smach.StateMachine.add('BAR', Bar(),
                               transitions={'outcome1': 'FOO'},
                               remapping={'first_in': 'sm_counter_1',
                                          'second_in' : 'sm_counter_2'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()