import RPi.GPIO as GPIO

PIN_CAMERA_IN = 18

class Switches:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_CAMERA_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    def get_value(self, callback):
        input_state = GPIO.input(18)
        if(input_state == False):
            print "photo!"
            return callback()

