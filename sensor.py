import sys
import Adafruit_DHT
import datetime

class Sensor:
    
    def requestReading(self):
        x = Reading()
        return x
    def printReadingC(self):
        d = self.requestReading()
        print d.getTemperature()," ",d.getHumidity(),"\t",datetime.datetime.now().time()
        
    def printReadingF(self):
        d = self.requestReading()
        tTemp =d.getTemperature() * 9/5 + 32 
        print "Temperature: ",tTemp,"F \t","Humidity: ",d.getHumidity(),"% ","  ",datetime.datetime.now().time()
        
        
        
class Reading:
    def __init__(self):
        self.humidity,self.temperature = Adafruit_DHT.read_retry(11, 4)

    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity

##sensor test handler

##def main():
##    print("Enter text (or Enter to quit): ")
##    while True:
##        r = Sensor()
##        r.printReadingF()
##        i = raw_input()
##        if i == "exit":
##            break
##    print("program halted")
##
##if __name__ == "__main__":
##    main()
    