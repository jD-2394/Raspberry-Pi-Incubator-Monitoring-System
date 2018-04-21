import Adafruit_DHT
import json
from threading import *
import threading
import time
import random





class Sensor:
    def __init__(self):
        self.TemperatureUnit = "Celsius"
        self.sensorDHT111 = SensorCore()
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, 4)
        #self.settingsFile = open('settings.json','w')
    def getHumidity(self):
        self.sensorDHT111 = SensorCore()
        humidity = self.sensorDHT111.getHumidity()
        return humidity

    def readSensor():
        self.sensorDHT111 = SensorCore()
        return self.sensorDHT111
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
    
    def getTemperatureUnit(self):
        #data = json.load(self.settingsFile)
        return self.TemperatureUnit
        #return data['temperatureUnit']
    
    def getTemperature(self):
        self.sensorDHT111 = SensorCore()
        unit = self.TemperatureUnit
        with open('/home/pi/Documents/DjangoProjects/core/pages/static/pages/settings.txt', 'r') as outfile:
            data = json.load(outfile)
            Nunit = data['TemperatureUnit']
        print("Sensor unit is: " + unit)
        #d = random.randint(0, 100)
        if unit == "Celsius":
            #return d
            return self.sensorDHT111.getTemperature()
        elif unit == "Farenheit":


            #d = self.requestReading()
            tTemp = self.sensorDHT111.getTemperature() * 9/5 + 32
            #tTemp =random.randint(0, 100) * 9/5 + 32
            return tTemp
        elif unit == "Kelvin":
            return self.sensorDHT111.getTemperature() + 273.15
        else:
            print ("temperature unit not specified")
            return None

class SensorCore:
    def __init__(self):
        self.humidity = 0
        self.temperature = 0
        try:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(11, 4)
        except:
            print('Sensor is not connect, check wiring')
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity

class temperatureUnits:
    FARENHEIT = 0
    CELSIUS = 1
    KELVIN = 2