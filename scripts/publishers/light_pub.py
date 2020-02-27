import rospy
from pub_state_test.msg import lights

class Light_publisher:
    def __init__(self):
        self.pub = rospy.Publisher('lights', lights, queue_size=1)
        self.lights_data = lights()

    def mode(self, mode):
        self.lights_data.mode = mode
        self.pub(self.lights_data)