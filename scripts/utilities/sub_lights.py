#!/usr/bin/env python


from led_strip import Led_Strip
import rospy
from pub_state_test.msg import lights

class Sub_lights():
    def __init__(self):
        #NUmber of lights
        num = 99
        self.light_strip = Led_Strip(99)
        self.light_strip.start()

        self.subscriber = rospy.Subscriber('light_data', lights, self.callback)

        self.modes = {'critical_error': self.critical_error, 'ready_state': self.ready_state,
                      'search_state':self.search_state, 'lights_off':self.lights_off,
                      'execute_state':self.execute_state, 'approach_state':self.approach_state}
        self.prev_mode = None

    def callback(self, data):
        mode = data.mode
        rospy.loginfo(mode)
        if (mode in self.modes) and mode!=self.prev_mode:
            self.prev_mode = mode
            self.modes[mode]()

    def critical_error(self):
        self.light_strip.set_mode('blinking_light', 'red')

    def ready_state(self):
        self.light_strip.set_mode('blinking_light', 'green')

    def search_state(self):
        self.light_strip.set_mode('scanning_light', 'teal')

    def approach_state(self):
        self.light_strip.set_mode('blinking_light', 'yellow')

    def execute_state(self):
        self.light_strip.set_mode('blinking_light', 'pink')

    def lights_off(self):
        self.light_strip.set_mode('solid_light', 'off')

def listener():
    rospy.init_node('sub_lights')
    sub_lights = Sub_lights()
    # sub_lights.ready_state()
    rospy.spin()


if __name__ == '__main__':
    listener()

