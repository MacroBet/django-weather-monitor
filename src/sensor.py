import RPi.GPIO as GPIO
import time
import os

PHOTORESISTOR_PIN = 7
MESURES_COUNT = 10

# Read Temperature and humidity
def readTandu(pin):
    result = os.popen('cd ./lib/Adafruit_DHT/examples/ \n sudo ./AdafruitDHT.py 11 '+str(pin)).read()

    x = result.split(';')

    if(len(x)==2):
        return({"success":True, "temperature":float(x[0]),"humidity":float(x[1]) })

    else:
        return({"success":False,"error":result})


def rc_time ():
    count = 0
  
    #Output on the pin for 
    GPIO.setup(PHOTORESISTOR_PIN, GPIO.OUT)
    GPIO.output(PHOTORESISTOR_PIN, GPIO.LOW)
    time.sleep(0.01)

    #Change the pin back to input
    GPIO.setup(PHOTORESISTOR_PIN, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(PHOTORESISTOR_PIN) == GPIO.LOW):
        count += 1
        
    return count

class Sensor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)


    def readLightLevel(self):
        averageValue = 0
        print("* start reading light level")
        for x in range(0, MESURES_COUNT):
            averageValue+= rc_time()
        averageValue = averageValue/MESURES_COUNT
        print("* reading completed, light level :"+str(averageValue))
        return averageValue

# Usage Example
s = Sensor()
s.readLightLevel()
print(readTandu(21))
