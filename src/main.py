from utils import Utils
from pprint import pprint
from beeper import Beeper
from sensor import Sensor
from saver import Saver
from eventManager import EventManager
import time
import _thread
import os

import RPi.GPIO as GPIO

pins= {"photoresistor" : 13, "tandu" : 21, "button" : 16,
      "red" : 26, "green" : 20, "white" : 19, }

RELEASE = True
START = True

def automaticReadJob(timer, self):
    if RELEASE :
        self.beeper.makeBeep("white",18,0.5,.5,True)
        time.sleep(18)
    #_thread.start_new_thread( runServer,(self,self))
 


    while True:
        print("runnning")
        try:
            time.sleep(timer)
            self.onButtonPress()
        except:
            print("something went wrong")
    self.running = False

def runServer(nulla,self):
    while True:
        self.beeper.makeBeep("red",3,0.2,.1)
        self.beeper.makeBeep("green",3,0.2,.1)
        self.beeper.makeBeep("red",2,0.2,.1)
        time.sleep(5)

        try:
            #os.system('sh serverLauncher.sh')
            os.system('cd /\ncd home/pi/progetto_unifi/ppm\npython3 manage.py runserver 192.168.43.8:8000')
        except:
            self.beeper.makeBeep("red",5,0.2,.1)
        self.beeper.makeBeep("green",5,0.2,.1)
def getMeasures(name, self):
    if(self.readingLock):
        self.errorBeeper.makeBeep("red",3,0.2,.1)
        return
    self.readingLock = True
    beeper = self.beeper
    sensorReader = self.sensorReader
    beeper.turnOn("green")
    brightness = sensorReader.readLightLevel()
    beeper.makeBeep("white",3,0.2,.1)
    tandu = sensorReader.readTandu()
    beeper.makeBeep("white",3,0.2,.1)
    timeStamp = sensorReader.takePhoto()
    beeper.makeBeep("white",3,0.2,.1)

    save='curl "http://192.168.43.8:8000/server/addone/?humidity='+str(tandu["humidity"])+'&brightness='+str(brightness)+'&temperature='+str(tandu["temperature"])+'&img_url='+timeStamp+'"'
 
    result = os.popen(save).read()
    print(result)
    if result=="fatto":
        beeper.makeBeep("white",3,0.2,.1)
    else:
        beeper.makeBeep("red",3,0.2,.1)


    beeper.turnOff("green")
    beeper.turnOn("white")
    self.readingLock = False

    self.saver.add_measure(tandu["temperature"],tandu["humidity"],brightness,timeStamp)
    
    self.kill()

def main():
    
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
        self.saver = Saver()

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
        timer = 60*60

        _thread.start_new_thread( automaticReadJob, (timer,self))
        time.sleep(3000000)
        print("Main Completed")

        

if START :     
    main = Main()
    main.run()

