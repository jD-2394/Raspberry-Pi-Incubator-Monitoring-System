#import Adafruit_DHT
import json
from threading import *
import threading
import time
import random


class ClimateThread(threading.Thread):
    def __init__(self):
        super(ClimateThread, self).__init__()
        self.humidity = 0
        self.temperature = 0
        self.running = False
        self.m = Lock()
        self.Cur_Sensor=Sensor()



    def getTemperature(self):
       # print("Get Temperature")
        self.m.acquire()
        s = self.temperature
        self.m.release()
        return s
    def getHumidity(self):
       # print("Get Humidity")
        self.m.acquire()
        s = self.humidity
        self.m.release()
        return s


    def run(self):
        print("Thread is running...")
        while True:
            self.m.acquire()
            self.humidity = self.Cur_Sensor.getHumidity() #placeholder for sensor input
            self.m.release()
            self.m.acquire()
            self.temperature = self.Cur_Sensor.getTemperature()  #placeholder for sensor input
            self.m.release()
            time.sleep(1) # wait a second






class Sensor:
    def __init__(self):
        self.TemperatureUnit = temperatureUnits.CELSIUS
        #self.settingsFile = open('settings.json','w')
    def getHumidity(self):
        #d = self.requestReading()
        d = random.randint(0,100)
        return d
        #return d.getHumidity()

    def setTemperatureUnit(self,unit):
        if(unit == "Celsius" or unit == "celsius"):
            self.TemperatureUnit = temperatureUnits.CELSIUS
            #data = json.load(self.settingsFile)
            #data['temperatureUnit']="Celsius"
        elif(unit == "Farenheit" or unit == "farenheit"):
            self.TemperatureUnit = temperatureUnits.FARENHEIT
            #data = json.load(self.settingsFile)
            #data['temperatureUnit'] = "Farenheit"
        elif(unit == "Kelvin" or unit == "kelvin"):
            self.TemperatureUnit = temperatureUnits.KELVIN
            #data = json.load(self.settingsFile)
            #data['temperatureUnit'] = "Kelvin"
        else:
            print ("please specify valid unit of temperature")
    
    def getTemperatureUnit(self):
        #data = json.load(self.settingsFile)
        return temperatureUnits
        #return data['temperatureUnit']
    
    def getTemperature(self):
        d = random.randint(0, 100)
        #d = self.requestReading()
        if self.TemperatureUnit == temperatureUnits.CELSIUS:
            return d
            #return d.getTemperature()
        elif self.TemperatureUnit == temperatureUnits.FARENHEIT:


            #d = self.requestReading()
            tTemp = d * 9 / 5 + 32
            #tTemp =random.randint(0, 100) * 9/5 + 32
            return tTemp
        elif self.TemperatureUnit == temperatureUnits.KELVIN:
            return d + 273.15
        else:
            print ("temperature unit not specified")
            return None



class temperatureUnits:
    FARENHEIT = 0
    CELSIUS = 1
    KELVIN = 2