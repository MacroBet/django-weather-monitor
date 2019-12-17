import RPi.GPIO as GPIO
import _thread
import time

BEEP_DURATION =.6
BEEP_DELAY =.2 

def threadJob(name, self):
    print ( name+ "started")
    while len(self.stack)>0 :
        beepInfo = self.stack.pop()
        color = beepInfo['color']
        beeps = beepInfo['beeps']
        duration = beepInfo['duration']
        delay = beepInfo['delay']
        while not beeps == 0 :
            time.sleep(delay)
            self.turnOn(color)
            time.sleep(duration)
            self.turnOff(color)
            beeps= beeps - 1
    self.threadRunning = False
    

class Beeper:
    def __init__(self):
        self.colors = {'red': 26 , 'green': 20, 'white': 19}
        self.threadRunning=False
        self.stack = list()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
    def isColorValid(self,color):
        return (color=="red" or color=="green" or color=="white")
        
    def turnOn(self,color):
        pin = self.colors[color]
        GPIO.setup(pin,GPIO.OUT)
        print ("LED "+color+" on")
        GPIO.output(pin ,GPIO.HIGH)

    def turnOff(self,color):
        pin = self.colors[color]
        GPIO.setup(pin,GPIO.OUT)
        print ("LED "+color+" off")
        GPIO.output(pin ,GPIO.LOW)

    def makeBeep(self, color, beeps, duration = BEEP_DURATION, delay = BEEP_DELAY):
        if(self.isColorValid(color)):
            self.stack.insert(0,{'color': color,"beeps": beeps, "duration":duration, "delay":delay })
            if(not self.threadRunning):
                self.threadRunning = True
                _thread.start_new_thread( threadJob, ("Beeper Thread",self)) 
            
            
# USAGE EXAMPLE
#b = Beeper()
#b1 = Beeper()
#b2 = Beeper()
#b.turnOn("white")
#b.makeBeep("red",3)
#b.makeBeep("green",3)
#b.makeBeep("white",10,.5,.3)

