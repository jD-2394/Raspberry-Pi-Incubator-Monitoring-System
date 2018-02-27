import sys
import Adafruit_DHT
import datetime
import json

class Sensor:
    
    
    
    
    def requestReading(self):
        x = Reading()
        return x
    def printReadingC(self):
        d = self.requestReading()
        if d.sensorConnected:    
            print d.getTemperature()," ",d.getHumidity(),"\t",datetime.datetime.now().time()
        else:
            print "Cannot print reading, Sensor not connected"
        
    def printReadingF(self):
        d = self.requestReading()
        if d.sensorConnected:    
            tTemp =d.getTemperature() * 9/5 + 32 
            print "Temperature: ",tTemp,"F \t","Humidity: ",d.getHumidity(),"% ","  ",datetime.datetime.now().time()
        else:
            print "Cannot print reading, Sensor not connected"
        
        
        
class Reading:
    
   
    
    def __init__(self):
        
        self.sensorConnected =  False
        
        try:
            self.humidity,self.temperature = Adafruit_DHT.read_retry(11, 4)
            sensorConnected = True
        except:
            print'Sensor not detected, check wiring'

    def getTemperature(self):
        if self.sensorConnected:
            return self.temperature
    def getHumidity(self):
        if self.sensorConnected:
            return self.humidity