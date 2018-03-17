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
        self.TemperatureUnit = unit
    
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
            print "please specify valid unit of temperature"
            return None
        
    
class Reading:
    
   
    
    def __init__(self):
        
        self.sensorConnected =  False
        
        try:
            self.humidity,self.temperature = Adafruit_DHT.read_retry(11, 4)
            if(self.humidity == None or self.temperature == None):
                print' sensor not connected'
        except:
            print'Sensor not detected, check wiring'

    def getTemperature(self):
            return self.temperature
    def getHumidity(self):
            return self.humidity
        
class temperatureUnits:
    FARENHEIT = 0
    CELSIUS = 1
    KELVIN = 2