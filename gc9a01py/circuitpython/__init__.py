class Pin:
    def __init__(self, pin: int):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.OUTPUT
    
    def off(self):
        self.pin.value = False
    
    def on(self):
        self.pin.value = True
    
    def value(self, value: int):
        self.pin.value = value
