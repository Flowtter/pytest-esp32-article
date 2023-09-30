class DHT22:
    def __init__(self, pin):
        self.pin = pin
        self.temp = None
        self.humi = None

    def measure(self):
        self.temp = 26.5
        self.humi = 48.0

    def temperature(self):
        return self.temp

    def humidity(self):
        return self.humi
