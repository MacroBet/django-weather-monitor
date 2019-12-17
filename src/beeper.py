import RPi.GPIO as GPIO
import _thread
import time

BEEP_DURATION =.6
BEEP_DELAY =.2
DEBUG = False

def threadJob(name, self):
    if DEBUG : 
        print ( name+ "started")
    while len(self.stack)>0 :
        beepInfo = self.stack.pop()
        color = beepInfo['color']
        beeps = beepInfo['beeps']
        duration = beepInfo['duration']
        delay = beepInfo['delay']
        leaveOn = beepInfo['leaveOn']

        while not beeps == 0 :
            time.sleep(delay)
            self._turnOn(color)
            time.sleep(duration)
            self._turnOff(color)
            beeps= beeps - 1
            
        if(leaveOn):
            self._turnOn(color)
            
    self.threadRunning = False
    

class Beeper:
    def __init__(self,colors):
        self.colors = colors
        self.threadRunning=False
        self.stack = list()
        
    def isColorValid(self,color):
        return (color=="red" or color=="green" or color=="white")
        
    def _turnOn(self,color):
        pin = self.colors[color]
        GPIO.setup(pin,GPIO.OUT)
        #print ("LED "+color+" on")
        GPIO.output(pin ,GPIO.HIGH)

    def _turnOff(self,color):
        pin = self.colors[color]
        GPIO.setup(pin,GPIO.OUT)
        #print ("LED "+color+" off")
        GPIO.output(pin ,GPIO.LOW)

    #public methods
    def turnOn(self,color):
        self.makeBeep(color,1,0.1,0.1,True)

    def turnOff(self,color):
        self.makeBeep(color,1,0.1,0.1,False)

    def makeBeep(self, color, beeps, duration = BEEP_DURATION, delay = BEEP_DELAY, leaveOn = False):
        if(self.isColorValid(color)):
            self.stack.insert(0,{'color': color,"beeps": beeps, "duration":duration, "delay":delay, "leaveOn": leaveOn })
            if(not self.threadRunning):
                self.threadRunning = True
                _thread.start_new_thread( threadJob, ("Beeper Thread",self)) 
            


###############################################

def __test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    b = Beeper({'red': 26 , 'green': 20, 'white': 19})
    b1 = Beeper({'red': 26 , 'green': 20, 'white': 19})
    b2 = Beeper({'red': 26 , 'green': 20, 'white': 19})
    b.turnOn("white")
    b.makeBeep("red",3)
    b.makeBeep("green",3)
    b.makeBeep("white",10,.5,.3)
#__test()

###############################################
