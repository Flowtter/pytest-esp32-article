import machine
import dht


class LedSwitcher:
    def __init__(self, green_led_pin):
        self.greenLed = machine.Pin(green_led_pin, machine.Pin.OUT)
        self.is_green = False
        self.greenLed.off()

    def toggle_led(self):
        if self.is_green:
            self.greenLed.off()
        else:
            self.greenLed.on()
        self.is_green = not self.is_green


class App:
    def __init__(self, sendor_pin, green_led_pin):
        self.sensor = dht.DHT22(machine.Pin(sendor_pin))
        self.led_switcher = LedSwitcher(green_led_pin)

    def run(self):
        self.led_switcher.toggle_led()
        self.sensor.measure()
        temperature = self.sensor.temperature()
        humidity = self.sensor.humidity()
        return temperature, humidity
