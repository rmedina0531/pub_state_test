#!/usr/bin/env python


# from led_strip import Led_Strip
import rospy
from comms import Subscriber

class Sub_lights():
    def __init__(self):
        #NUmber of lights
        # num = 99
        # self.lights = Led_Strip(99)
        # self.lights.start()

        # self.subscriber = rospy.Subscriber('lights', lights, self.callback)
        self.sub = Subscriber('light_data', 'light_data')

        self.modes = {'critical_error': self.critical_error, 'ready_state': self.ready_state,
                      'search_state':self.ready_state, 'lights_off':self.lights_off, 'stand_by':self.stand_by}

    def callback(self, data):
        rospy.loginfo(data.mode)
        if data.mode in self.modes:
            self.modes[mode]()

    def critical_error(self):
        self.lights.execute('blinking_light', 'red')

    def ready_state(self):
        self.lights.execute('blinking_light', 'green')

    def search_state(self):
        self.lights.execute('scanning_light', 'teal')

    def lights_off(self):
        self.lights.execute('solid_light', 'off')

    def stand_by(self):
        self.lights.execute('blinking_light', 'blue')

def listener():
    rospy.init_node('sub_lights')
    sub_lights = Sub_lights()
    rospy.spin()

if __name__ == '__main__':
    listener()
