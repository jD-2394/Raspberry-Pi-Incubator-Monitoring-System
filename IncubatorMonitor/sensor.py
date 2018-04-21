import Adafruit_DHT
import json
from threading import *
import threading
import time
import random

class Sensor:
    def __init__(self):
        self.TemperatureUnit = "Celsius"
        self.S_Core = SensorCore()
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, 4)
        #self.settingsFile = open('settings.json','w')
    def getHumidity(self):
        #d = random.randint(0,100)
        #return d
        return self.humidity

    def setTemperatureUnit(self,unit):
        print("Unit to set is: " + unit)  
        if(unit == "Celsius" or unit == "celsius"):
            self.TemperatureUnit = "Celsius"
            #data = json.load(self.settingsFile)
            #data['temperatureUnit']="Celsius"
        elif(unit == "Farenheit" or unit == "farenheit"):
            self.TemperatureUnit = "Farenheit"
            #data = json.load(self.settingsFile)
            #data['temperatureUnit'] = "Farenheit"
        elif(unit == "Kelvin" or unit == "kelvin"):
            self.TemperatureUnit = "Kelvin"
            #data = json.load(self.settingsFile)
            #data['temperatureUnit'] = "Kelvin"
        else:
            print ("please specify valid unit of temperature")
    def getRawTemp(self):
        return self.S_Core.getTemperature
    
    def getTemperatureUnit(self):
        #data = json.load(self.settingsFile)
        return self.TemperatureUnit
        #return data['temperatureUnit']
    
    def getTemperature(self):
        unit = ""
        with open('/home/pi/Documents/DjangoProjects/core/pages/static/pages/settings.txt', 'r') as outfile:
            data = json.load(outfile)
            unit = data['TemperatureUnit']
        print("Sensor unit is: " + unit)
        #d = random.randint(0, 100)
        if unit == "Celsius":
            #return d
            return self.temperature
        elif unit == "Farenheit":


            #d = self.requestReading()
            tTemp = self.temperature * 9/5 + 32
            #tTemp =random.randint(0, 100) * 9/5 + 32
            print("Temperature @ Sensor is" + tTemp)
            return tTemp
        elif unit == "Kelvin":
            return self.temperature + 273.15
        else:
            print ("temperature unit not specified")
            return None

class SensorCore:
    def __init__(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, 4)
    
    def getTemperature(self):
        temperazture = Adafruit_DHT.read_retry(11, 4)
        return temperature
    def getHumidity(self):
        self.humidity = Adafruit_DHT.read_retry(11, 4)
        return self.humidity

class temperatureUnits:
    FARENHEIT = 0
    CELSIUS = 1
    KELVIN = 2