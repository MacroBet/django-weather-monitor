import RPi.GPIO as GPIO
import time
import os
from picamera import PiCamera
from utils import Utils

MESURES_COUNT = 10

def _getLightMesure (pin):
    count = 0
    
    #Output on the pin for 
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.01)

    #Change the pin back to input
    GPIO.setup(pin, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1
        
    return count

class Sensor:
    def __init__(self, photoresistorPin, tanduPin):
        self.photoresistorPin = photoresistorPin
        self.tanduPin = tanduPin

    def readLightLevel(self):
        averageValue = 0
        print("* start reading light level")
        for x in range(0, MESURES_COUNT):
            averageValue+= _getLightMesure(self.photoresistorPin)
        averageValue = averageValue/MESURES_COUNT
        print("* reading completed, light level :"+str(averageValue))
        return averageValue

    # Read Temperature and humidity
    def readTandu(self):
        print("* start reading temperature and humidity")
        result = os.popen('cd ./lib/Adafruit_DHT/examples/ \n sudo ./AdafruitDHT.py 11 '+str(self.tanduPin)).read()
        x = result.split(';')
        result = {}
        
        if(len(x)==2):
            result = {"success":True, "temperature":float(x[0]),"humidity":float(x[1]) }
        else:
            result = {"success":False,"error":result}

        print("* reading completed, result :"+str(result))
        return result

    def takePhoto(self):
        camera = PiCamera()
        timeStamp = Utils.getTimeStamp()
        camera.capture('../ppm/server/static/server/images/plant/'+timeStamp+'.jpg',"jpeg",False,None,0,False)
        camera.close()
        print("* photo taken: "+timeStamp+".jpg")
        return timeStamp

###############################################

def __test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    s = Sensor(13, 21)
    s.readLightLevel()
    s.readTandu()
    timeStamp = s.takePhoto()

#__test()

###############################################
