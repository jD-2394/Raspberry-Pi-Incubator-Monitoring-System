import time
import sys
from enum import Enum

class defaultValues(Enum):
    CHICKEN_EGG_LOWER_TEMPERATURE_C = 95.5
    CHICKEN_EGG_UPPER_TEMPERATURE_C = 97.5
    CHICKEN_EGG_HUMIDITY = 70.0
    
class eggSize(Enum):
    QUAIL = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    JUMBO = 4
class birdEggType(Enum):
    CHICKEN = 100
    TURKEY = 101
    QUAIL = 102
    EMU = 103
    OSTRICH = 104

class eggBatch:
    def __init__(self,hi = defaultValues.CHICKEN_EGG_UPPER_TEMPERATURE_C,lo = defaultValues.CHICKEN_EGG_LOWER_TEMPERATURE_C,hum = defaultValues.CHICKEN_EGG_HUMIDITY,tInt = 0):
        #egg environment variables
        self.daysremaining = 0
        self.timeTilNextTurn = 0
        self.maximumTemperature = hi
        self.minimumTemperature = lo
        self.requiredHumidity = hum
        self.turnInterval = tInt
        #egg specific information - for now will assume only 1 breed
        self.EggsInBatch = []

    def getDaysRemaining(self): # how many days until next hatch
        return 0
    def getTimeUntilNextTurn(self): # how much time until eggs should be turned
        return timeTilNextTurn
    def setTurnInterval(self,interval): # set the turn interval in number of times per day
        turnInterval = 24/interval
        return 0
    def getMaximumTemperature(self): #maximum temperature for current batch of eggs
        return maximumTemperature
    def getMinumumTemperature(self): #get the minimum temperature for current batch of eggs
        return MinumumTemperature
    def addEgg(self,breed,eggType = birdEggType.CHICKEN,eggSiz = eggSize.MEDIUM):
        eggNumber = len(self.EggsInBatch) + 1
        eggToAdd = Egg(breed,eggNumber,eggType,eggSiz)
        self.EggsInBatch.append(eggToAdd)
    def removeEgg(self,eggNumberToRemove):
        self.EggsInBatch.pop(eggNumberToRemove)
    def getEggList(self):
        return self.EggsInBatch
        
    def printEggList(self):
        print 'This incubator has:'
        L = self.getEggList()
        for x in L:
            print 'egg Number: ' , x.eggNumber , 'type: ' , x.TypeOfEgg , 'size: ' , x.sizeOfEgg , 'breed: ', x.birdBreed 
    

    


class Egg:
    def __init__(self,breed,numberEg = 0,eggType = birdEggType.CHICKEN,eggSiz = eggSize.MEDIUM):
        self.eggNumber = numberEg
        self.TypeOfEgg = eggType
        self.sizeOfEgg = eggSiz
        self.birdBreed = breed
    

    
        
        
    
    
    

