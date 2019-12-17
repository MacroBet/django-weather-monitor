#from mongo import Mongo
from utils import Utils
from pprint import pprint
from beeper import Beeper
from sensor import Sensor
from eventManager import EventManager
import time
import _thread

import RPi.GPIO as GPIO

pins= {"photoresistor" : 13, "tandu" : 21, "button" : 16,
      "red" : 26, "green" : 20, "white" : 19, }

def getMeasures(name, self):
    if(self.readingLock):
        self.errorBeeper.makeBeep("red",3,0.2,.1)
        return
    self.readingLock = True
    beeper = self.beeper
    sensorReader = self.sensorReader
    beeper.turnOn("green")
    sensorReader.readLightLevel()
    beeper.makeBeep("white",3,0.2,.1)
    sensorReader.readTandu()
    beeper.makeBeep("white",3,0.2,.1)
    timeStamp = sensorReader.takePhoto()
    beeper.makeBeep("white",3,0.2,.1)
    beeper.turnOff("green")
    beeper.turnOn("white")
    self.readingLock = False
    self.kill()

def main():
    m=Mongo()
    m.add_measure(20,74.6,12)
    #m.delete_all_measures() #BE CAREFUL WITH THAT

    from_date=Utils.create_date(2019,10,13,20,56,25)
    to_date= Utils.create_date(2020,1,1)

    cursor = m.get_measures(from_date,to_date)

    for document in cursor: 
        pprint(document)




class Main:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.beeper = Beeper(pins)
        self.errorBeeper = Beeper(pins)
        self.sensorReader = Sensor(pins["photoresistor"], pins["tandu"])
        self.readingLock = False
        evm = EventManager(pins["button"])
        evm.registerButtonListener(self.onButtonPress)
        self.running = True

    def __del__(self):
        runBeeper.turnOff("white")
        
    def onButtonPress(self):
        _thread.start_new_thread( getMeasures, ("Misurator Thread",self))
        
    def kill(self):
        self.running = False

    def run(self):
        print("Main Started")
        self.beeper.makeBeep("red",2,0.2,.1)
        self.beeper.makeBeep("green",2,0.2,.1)
        self.beeper.makeBeep("white",2,0.2,.1,True)
        while self.running:
            time.sleep(10)
        

    
main = Main()
main.run()

