import threading
from neopixel import *
import time


class Led_Strip(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.COLOR = {'red': Color(0, 255, 0), 'green': Color(255, 0, 0), 'blue': Color(0, 0, 255),
                 'yellow': Color(252, 252, 27), 'teal': Color(255, 27, 233),
                 'pink': Color(27, 252, 162), 'off': Color(0, 0, 0), 'white': Color(127, 127, 127)}

        self.MODES = {'solid_light':self.solid_light, 'blinking_light':self.blinking_light,
                      'color_wipe':self.color_wipe, 'scanning_light':self.scanning_light}

        self.mutex = threading.Lock()
        self.mode = None

        self.color = self.COLOR['off']
        self.change_pattern = False

        LED_PIN = 18
        self.led_strip = Adafruit_NeoPixel(num, LED_PIN)
        self.led_strip.begin()


        self._execute = self.solid_light


    def run(self):

        # try:
        #     while True:
        #         print(self.blinking_light(self.COLOR['blue']))
        # except:
        #     self.lights_off()

        while True:
            ##checks to see if the flag for change is true to change color pattern mode
            while True:
                self.mutex.acquire()
                execute = self._execute
                color = self.color
                self.mutex.release()

                if execute(color):
                    break

            ##run when there is a pattern change
            # print('pattern Change')
            self.lights_off()
            self.mutex.acquire()
            self._execute = self.MODES[self.mode]
            self.change_pattern = False
            self.mutex.release()


    def lights_off(self):
        for i in range(self.led_strip.numPixels()):
            self.led_strip.setPixelColor(i, self.COLOR['off'])
        self.led_strip.show()
        return self.wait_event(10)

    def set_mode(self, mode, color=Color(0,0,255)):
        print('setMode')
        if mode in self.MODES:
            self.mutex.acquire()
            self.mode = mode
            self.color = self.COLOR[color]
            self.change_pattern = True
            self.mutex.release()

    def wait_event(self, time_seconds):
        rate = 1 #in millaseconds
        loops = int((1000.0/rate) * time_seconds)
        for i in range(loops):
            # print(i)
            # print(loops)
            self.mutex.acquire()
            change = self.change_pattern
            self.mutex.release()
            if change:
                return True
            # print('before sleep')
            time.sleep(rate/1000.0)
            # print('after sleep')
        return False


    def solid_light(self, color):
        for i in range(self.led_strip.numPixels()):
            self.led_strip.setPixelColor(i, color)
        self.led_strip.show()
        return self.wait_event(10)

    def blinking_light(self, color):
        for i in range(self.led_strip.numPixels()):
            self.led_strip.setPixelColor(i, color)
        # print('change color1')
        self.led_strip.show()

        if self.wait_event(.8):
            return True

        for i in range(self.led_strip.numPixels()):
            self.led_strip.setPixelColor(i, self.COLOR['off'])
        self.led_strip.show()

        if self.wait_event(.8):
            return True

        return False

    def color_wipe(self, color):
        #100ms
        for i in range(self.led_strip.numPixels()):
            self.led_strip.setPixelColor(i, color)
            self.led_strip.show()
            if self.wait_event(1):
                return True
        return False

    def scanning_light(self, color, length=6, time_seconds=12/1000.0):
        #options[color, length, time_ms]
        first = 0
        for i in range(length + 1):
            self.led_strip.setPixelColor(i, color)

        while True:
            while first < self.led_strip.numPixels():
                first += 1
                self.led_strip.setPixelColor(first, color)
                self.led_strip.setPixelColor(first - length, self.COLOR["off"])
                self.led_strip.show()
                if self.wait_event(time_seconds):
                    return True

            while (first - length) >= 0:
                self.led_strip.setPixelColor(first - length, color)
                self.led_strip.setPixelColor(first, self.COLOR["off"])
                self.led_strip.show()
                if self.wait_event(time_seconds):
                    return True
                first -= 1