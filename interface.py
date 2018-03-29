from eggTracker import eggBatch
from sensor import Reading
import datetime

class systemInterface():
    def __init__(self):
        self.currentSensor = Reading()
        self.currentBatch = eggBatch()

    # *******************************************************************
    # Temperature Interface Controls
    # *******************************************************************


    def setTemperatureUnits(self,unitToSet):
        self.currentSensor.setTemperatureUnit(unitToSet)
    def getTemperatureUnits(self):
        return self.currentSensor.getTemperatureUnit

    def getTemperature(self):
       return self.currentSensor.getTemperature()
    def getHumidity(self):
        return self.currentSensor.getHumidity()

    # *******************************************************************
    # Egg Information Interface Controls
    # *******************************************************************

    def createEggBatch(self,highTemp,loTemp,minHum,maxHum,turnInterval):
        self.currentBatch = eggBatch(highTemp,loTemp,minHum,maxHum,turnInterval)
    def deleteEggBatch(self):
        self.currentBatch = None

    def addEggToBatch(self,breed,eggType = None,eggSiz = None):
        self.addEggToBatch(breed,eggType,eggSiz)
    def removeEgg(self,eggNumberToRemove):
        self.removeEgg(eggNumberToRemove)

    def getEggList(self):
        return self.currentBatch.getEggList()

    def printEggList(self):
        print 'This incubator has:'
        L = self.getEggList()
        for x in L:
            print 'egg Number: ' , x.eggNumber , 'type: ' , x.TypeOfEgg , 'size: ' , x.sizeOfEgg , 'breed: ', x.birdBreed

    # *******************************************************************
    # Time Interface Controls
    # *******************************************************************


    def getTurnTime(self):
        return self.currentBatch.timeTilNextTurn()
    def setTurnTime(self,interval):
        self.currentBatch.setTurnInterval(interval)

    def setHatchTime(self,days):
        self.setHatchTime(days)
    def getHatchTime(self):
        return self.currentBatch.getTimeUntilHatch()

    def startTurnTime(self):
        self.currentBatch.startEggTurnInterval()
    def startHatchTime(self):
        self.currentBatch.startHatchTimer()

    def getSystemTime(self):
        return datetime.datetime.now()

#*******************************************************************
# Settings Controls
# *******************************************************************




