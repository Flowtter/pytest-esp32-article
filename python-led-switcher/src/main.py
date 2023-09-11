import time
import machine

class LedSwitcher:
    def __init__(self, green_led_pin, red_led_pin):
        self.greenLed = machine.Pin(green_led_pin, machine.Pin.OUT)
        self.redLed = machine.Pin(red_led_pin, machine.Pin.OUT)

    def green(self):
        self.greenLed.on()
        self.redLed.off()

    def red(self):
        self.greenLed.off()
        self.redLed.on()
