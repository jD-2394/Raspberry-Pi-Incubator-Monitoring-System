import Adafruit_DHT

class Sensor:
    def __init__(self):
        self.TemperatureUnit = temperatureUnits.CELSIUS
    
    def requestReading(self):
        x = Reading()
        return x
    def getHumidity(self):
        d = self.requestReading()
        return d.getHumidity()
    
    def setTemperatureUnit(self,unit):
        if(unit == "Celsius" or unit == "celsius"):
            self.TemperatureUnit = temperatureUnits.CELSIUS
        elif(unit == "Farenheit" or unit == "farenheit"):
            self.TemperatureUnit = temperatureUnits.FARENHEIT
        elif(unit == "Kelvin" or unit == "kelvin"):
            self.TemperatureUnit = temperatureUnits.KELVIN
        else:
            print "please specify valid unit of temperature"
    
    def getTemperatureUnit(self):
        return self.TemperatureUnit
    
    def getTemperature(self):
        d = self.requestReading()
        if self.TemperatureUnit == temperatureUnits.CELSIUS:
            return d.getTemperature()
        elif self.TemperatureUnit == temperatureUnits.FARENHEIT:
            d = self.requestReading()
            tTemp =d.getTemperature() * 9/5 + 32
            return tTemp
        elif self.TemperatureUnit == temperatureUnits.KELVIN:
            return d.getTemperature() + 273.15
        else:
            print "temperature unit not specified"
            return None
        
    
class Reading:
    
   
    
    def __init__(self):
        
        self.sensorConnected =  False

        self.humidity,self.temperature = Adafruit_DHT.read_retry(11, 4)
        if(self.humidity == None or self.temperature == None):
            print' sensor not connected'

    def getTemperature(self):
            return self.temperature
    def getHumidity(self):
            return self.humidity
        
class temperatureUnits:
    FARENHEIT = 0
    CELSIUS = 1
    KELVIN = 2