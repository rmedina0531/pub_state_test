#! /usr/bin/env python
import rospy

from std_msgs.msg import Int32

def publisher_count():
    rospy.init_node('counter')

    pub=rospy.Publisher('count', Int32, queue_size=10)

    rate=rospy.Rate(10)

    current = 0;
    while True:
        rospy.loginfo(current)
        pub.publish(current)
        current += 1
        rate.sleep()

if __name__=='__main__':
    publisher_count()