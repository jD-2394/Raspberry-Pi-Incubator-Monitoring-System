from .eggTracker import *
from .sensor import *
import datetime

class systemInterface():
    def __init__(self):
        self.currentSensor = Sensor()
        self.currentBatch = eggBatch()

    # *******************************************************************
    # Temperature Interface Controls
    # *******************************************************************

    def setTemperatureUnits(self,unitToSet):
        self.currentSensor.setTemperatureUnit(unitToSet)
    def getTemperatureUnits(self):
        return self.currentSensor.getTemperatureUnit()

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

    def addEggToBatch(self,breed,eggType = None,eggSize = None):
        breedEgg = breed
        TypeOfEgg = None
        Size = None

        if eggType == "Chicken" or eggType == "chicken" or eggType == "CHICKEN":
            TypeOfEgg = "Chicken"
            ValidChoice = True
        elif eggType == "Turkey" or eggType == "turkey" or eggType == "TURKEY":
            TypeOfEgg = "Turkey"
            ValidChoice = True
        elif eggType == "Quail" or eggType == "quail" or eggType == "QUAIL":
            TypeOfEgg = "Quail"
            ValidChoice = True
        elif eggType == "Emu" or eggType == "emu" or eggType == "EMU":
            TypeOfEgg = "Emu"
            ValidChoice = True
        elif eggType == "Ostrich" or eggType == "ostrich" or eggType == "OSTRICH":
            TypeOfEgg = "Ostrich"
            ValidChoice = True
        else:
            print (eggType, "is Invalid...")
            print ("Please enter an valid egg Type!")

        if eggSize == "Quail" or eggSize == "quail" or eggSize == "QUAIL":
            Size = "Quail"
            ValidChoice = True
        elif eggSize == "Small" or eggSize == "small" or eggSize == "SMALL":
            Size = "Small"
            ValidChoice = True
        elif eggSize == "Medium" or eggSize == "medium" or eggSize == "MEDIUM":
            Size = "Medium"
            ValidChoice = True
        elif eggSize == "Large" or eggSize == "large" or eggSize == "LARGE":
            Size = "Large"
            ValidChoice = True
        elif eggSize == "Jumbo" or eggSize == "jumbo" or eggSize == "JUMBO":
            Size = "Jumbo"
            ValidChoice = True
        else:
            print (eggSize, "is Invalid...")
            print ("Please enter an valid egg size!")
        print(breed," ",TypeOfEgg," ", Size )
        newEgg = Egg(breed,0, TypeOfEgg, Size)
        self.currentBatch.addEgg(newEgg)

    def removeEgg(self,eggNumberToRemove):
        self.currentBatch.removeEgg(eggNumberToRemove)

    def getEggList(self):
        return self.currentBatch.getEggList()

    def printEggList(self):
        print ('This incubator has:')
        L = self.getEggList()
        for x in L:
            print ('egg Number: ' , x.eggNumber , 'type: ' , x.TypeOfEgg , 'size: ' , x.sizeOfEgg , 'breed: ', x.birdBreed)

    # *******************************************************************
    # Time Interface Controls
    # *******************************************************************



#*******************************************************************
# Settings Controls
# *******************************************************************




