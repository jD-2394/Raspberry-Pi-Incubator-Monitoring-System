from eggTracker import eggBatch
from sensor import Reading

class systemInterface():
    def __init__(self):
        self.currentSensor = Reading()
        self.currentBatch = eggBatch()
        self.cur

    def setTemperatureUnits(self,unitToSet):
        self.currentSensor.setTemperatureUnit(unitToSet)
    def getTemperatureUnits(self):
        return self.currentSensor.getTemperatureUnit

    def getTemperature(self):
        self.currentSensor.getTemperature()
    def getHumidity(self):
        self.currentSensor.getHumidity()


    def createEggBatch(self,highTemp,loTemp,minHum,maxHum,turnInterval):
        self.currentBatch = eggBatch(highTemp,loTemp,minHum,maxHum,turnInterval)
    def deleteEggBatch(self):
        self.currentBatch = None

    def addEggToBatch(self,breed,eggType = None,eggSiz = None):
        self.addEggToBatch(breed,eggType,eggSiz)
    def removeEgg(self,eggNumberToRemove):
        self.removeEgg(eggNumberToRemove)

    def getEggList(self):
        self.getEggList()

    






    def getTurnTime(self):
        self.currentBatch.timeTilNextTurn()
    def setTurnTime(self,interval):
        self.currentBatch.setTurnInterval(interval)

    def setHatchTime(self,days):
        self.setHatchTime(days)
    def getHatchTime(self):
        self.currentBatch.getTimeUntilHatch()

    def startTurnTime(self):
        self.currentBatch.startEggTurnInterval()
    def startHatchTime(self):
        self.startTurnTime()




