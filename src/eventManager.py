import RPi.GPIO as GPIO
import _thread

BUTTON_PIN = 16
REFRESH_RATE = 1

def threadJob(name, self):
    print ( name+ "started")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while self.running :
        if(GPIO.input(16)==1):
            self.pressed = True
        else:
            if(self.pressed ):
                print("Button Pressed")
                self.pressed = False
                if(self.onPress is not None):
                    self.onPress()
        

class EventManager:
    def __init__(self):
        self.onPreess = None
        self.running = True
        self.pressed = False
        _thread.start_new_thread( threadJob, ("Event Manager Thread",self))

    def registerButtonListener(self, onPress):
        self.onPress = onPress

    def killThread(self):
        self.runnning = False


from led import Beeper

def beep():
    beeper = Beeper()
    beeper.makeBeep("white",3,0.4,.2)
    
evm = EventManager()
evm.registerButtonListener(beep)
