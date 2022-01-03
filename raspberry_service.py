import RPi.GPIO as GPIO


class RaspberryService:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.relay_pin = 8
        GPIO.setup(self.relay_pin, GPIO.OUTPUT)

    @property
    def on(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)
        return self.relay_pin

    @property
    def of(self):
        GPIO.output(self.relay_pin, GPIO.LOW)
        return self.relay_pin
