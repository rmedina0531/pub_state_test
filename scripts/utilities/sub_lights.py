#!/usr/bin/env python


# from led_strip import Led_Strip
import rospy
from pub_state_test.msg import lights

class Sub_lights():
    def __init__(self):
        #NUmber of lights
        # num = 99
        # self.lights = Led_Strip(99)
        # self.lights.start()

        self.subscriber = rospy.Subscriber('lights', lights, self.callback)

        self.modes = {'critical_error': self.critical_error, 'ready_state': self.ready_state,
                      'search_state':self.ready_state, 'lights_off':self.lights_off}

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

def listener():
    rospy.init_node('sub_lights')
    sub_lights = Sub_lights()
    rospy.spin()


if __name__ == '__main__':
    listener()
    # try:
    #     sub_lights = Sub_lights()
    #     # time.sleep(1)
    #     # sub_lights.set_mode('scanning_light', 'pink')
    #     # time.sleep(.5)
    #     # sub_lights.set_mode('blinking_light' , 'yellow')
    #     # time.sleep(.5)
    #     # sub_lights.set_mode('blinking_light', 'blue')
    #     # sub_lights.set_mode('solid_light', 'pink')
    #     # print('first')
    #     # time.sleep(5)
    #     # print('second')
    #     # sub_lights.set_mode('solid_light', 'green')
    #     # print('third')
    #     # time.sleep(5)
    #     # print('fourth')
    #     # sub_lights.set_mode('solid_light', 'red')
    #     # print('fifth')
    #     # # while True:
    #     # #     sub_lights.ready_state()
    #     # #     time.sleep(10)
    #     # #     sub_lights.search_state()
    #     # #     time.sleep(10)
    #     # #     sub_lights.critical_error()
    #     # #     time.sleep(10)
    # except KeyboardInterrupt:
    #         sub_lights.lights_off()
