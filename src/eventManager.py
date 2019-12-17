import RPi.GPIO as GPIO
import _thread

REFRESH_RATE = 1
DEBUG = False

def threadJob(name, self):
    print ( name+ "started")
    GPIO.setup(self.pinButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while self.running :
        if(GPIO.input(self.pinButton)==1):
            self.pressed = True
        else:
            if(self.pressed ):
                if DEBUG: 
                    print("Button Pressed")
                self.pressed = False
                if(self.onPress is not None):
                    self.onPress()
        

class EventManager:
    def __init__(self, pinButton):
        self.onPreess = None
        self.running = True
        self.pressed = False
        self.pinButton = pinButton
        _thread.start_new_thread( threadJob, ("Event Manager Thread",self))

    def registerButtonListener(self, onPress):
        self.onPress = onPress

    def killThread(self):
        self.runnning = False


from beeper import Beeper

###############################################

def __beep():
    beeper = Beeper()
    beeper.makeBeep("green",3,0.4,.2)
def __test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    evm = EventManager(16)
    evm.registerButtonListener(__beep)

#__test()

###############################################
