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
    def __init__(self, hiTemp = defaultValues.CHICKEN_EGG_UPPER_TEMPERATURE_C, loTemp = defaultValues.CHICKEN_EGG_LOWER_TEMPERATURE_C, minHumidity = defaultValues.CHICKEN_EGG_HUMIDITY,maxHumidity = defaultValues.CHICKEN_EGG_HUMIDITY, tInt = 0):
        #egg environment variables
        self.maximumTemperature = hiTemp
        self.minimumTemperature = loTemp
        self.minimumRequiredHumidity = minHumidity
        self.maximumRequiredHumidity = maxHumidity

        #egg time varaibles

        self.timeUntilHatch = 0
        self.timeTilNextTurn = 0
        self.eggTurnInterval = 0

        #egg turn variables
        self.turnInterval = tInt
        #store information about each egg in batch
        self.EggsInBatch = []
        #store information about possible breeds
#*******************************************************************
# Time commands
#*******************************************************************


# *******************************************************************
# Temperature/Humidity Commands
# *******************************************************************
    def getMaximumTemperature(self): #maximum temperature for current batch of eggs
        return self.maximumTemperature
    def getMinumumTemperature(self): #get the minimum temperature for current batch of eggs
        return self.minimumTemperature

    def getMaximumHumidity(self):
        return self.maximumRequiredHumidity
    def getMinimumHumidity(self):
        return self.minimumRequiredHumidity


# *******************************************************************
# Egg Information Commands
# *******************************************************************
    def addEgg(self,eggToAdd):
        eggToAdd.eggNumber = len(self.EggsInBatch) + 1
        self.EggsInBatch.append(eggToAdd)
    def removeEgg(self,eggNumberToRemove):
        self.EggsInBatch.pop(eggNumberToRemove)

    def getEggList(self):
        return self.EggsInBatch
    def printEggList(self):
        print ('This incubator has:')
        L = self.getEggList()
        for x in L:
            print ('egg Number: ' , x.eggNumber , 'type: ' , x.TypeOfEgg , 'size: ' , x.sizeOfEgg , 'breed: ', x.birdBreed)


class Egg:
    def __init__(self,breed,numberEg = 0,eggType = birdEggType.CHICKEN,eggSiz = eggSize.MEDIUM):
        self.eggNumber = numberEg
        self.TypeOfEgg = eggType
        self.sizeOfEgg = eggSiz
        self.birdBreed = breed
    

    
        
        
    
    
    

