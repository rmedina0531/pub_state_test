#!/usr/bin/env python
import rospy
import time

from std_msgs.msg import Float32

def timer():
	#publisher information
	rospy.init_node('clock')

	pub = rospy.Publisher('elapsed_time', Float32, queue_size=10)
	#print at 4 cycles a second	
	rate = rospy.Rate(4)

	current_time = 0

	while not rospy.is_shutdown():
		rate.sleep()
		current_time = current_time + .25
		
		rospy.loginfo(current_time)
		pub.publish(current_time)
		

if __name__ =='__main__':
	timer()
