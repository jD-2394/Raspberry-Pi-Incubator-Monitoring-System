from sensor import Sensor
from sensor import temperatureUnits
from Timer import IncubatorTimer
from eggTracker import eggBatch, birdEggType, eggSize,Egg
from interface import systemInterface
import thread
import datetime
import numbers


current_temperature = 0
current_humidity = 0
current_HatchTime = datetime.time(0,0,0,0)
current_TurnTime = datetime.time(0,0,0,0)

curSysInterface = systemInterface()
currentEggList = curSysInterface.getEggList()


def temperatureService():
    while True:
        curSysInterface.getTemperature()
        curSysInterface.getHumidity()

def timerService():
    while True:
        curSysInterface.getHatchTime()
        curSysInterface.getTurnTime()

def systemService():
    while True:
        i = raw_input("Select an option: 1 Add egg to incubator  2 Remove egg from incubator 3 print incubator list 4 clear incubator list")
        if i == 1:
            print("Add egg:")
            eggBreed = None
            eggType = None
            Size = None
            z = raw_input("Enter Egg Breed:")
            eggBreed = z
            x = raw_input("Enter egg Type")
            ValidChoice = False
            while ValidChoice == False:
                if x == "Chicken" or x == "chicken" or x == "CHICKEN":
                    eggType = birdEggType.CHICKEN
                    ValidChoice = True
                elif x == "Turkey" or x == "turkey" or x == "TURKEY":
                    eggType = birdEggType.TURKEY
                    ValidChoice = True
                elif x == "Quail" or x == "quail" or x == "QUAIL":
                    eggType = birdEggType.QUAIL
                    ValidChoice = True
                elif x == "Emu" or x == "emu" or x == "EMU":
                    eggType = birdEggType.EMU
                    ValidChoice = True
                elif x == "Ostrich" or x == "ostrich" or x == "OSTRICH":
                    eggType = birdEggType.OSTRICH
                    ValidChoice = True
                else:
                    print ("Please enter an valid egg Type!")
            y = raw_input("Enter egg Size")
            ValidChoice = False
            while ValidChoice == False:
                if x == "Quail" or x == "quail" or x == "QUAIL":
                    Size = eggSize.QUAIL
                    ValidChoice = True
                elif x == "Small" or x == "small" or x == "SMALL":
                    Size = eggSize.SMALL
                    ValidChoice = True
                elif x == "Medium" or x == "medium" or x == "MEDIUM":
                    Size = eggSize.MEDIUM
                    ValidChoice = True
                elif x == "Large" or x == "large" or x == "LARGE":
                    Size = eggSize.LARGE
                    ValidChoice = True
                elif x == "Jumbo" or x == "jumbo" or x == "JUMBO":
                    Size = eggSize.JUMBO
                    ValidChoice = True
                else:
                    print ("Please enter an valid egg size!")
            newEgg = Egg(eggBreed,eggType,Size)
            curSysInterface.addEggToBatch(newEgg)
            currentEggList = systemInterface.getEggList()

        elif i == 2:
            print("Remove egg:")
            ValidChoice = False
            while ValidChoice == False:
                z = raw_input("Enter number of egg you wish to remove")
                if len(currentEggList) == 0:
                    print ("No Eggs to Remove")
                    ValidChoice = True
                elif z > len(currentEggList) or z < 0:
                    print ("Egg does not exist in list")
                    ValidChoice = True
                elif isinstance(x,numbers.Integral) == False:
                    print ("Invalid index, try again!")
                    ValidChoice = True
                else:
                    currentEggList.pop(z)
                    print ("Egg at index ", z," Has been removed!")
                    currentEggList = systemInterface.getEggList()


        elif i == 3:
                systemInterface.printEggList()
        elif i == 4:
            print("Clearing List...")
            currentEggList = eggBatch.getEggList()
            print ("List Cleared")
        else:
            print("Please input an valid selection")



def main():
    climate = None
    timer = None
    system = None

    climate = thread.start_new_thread(temperatureService())
    timer = thread.start_new_thread(timerService())
    system = thread.start_new_thread(systemService)


    climate.start()
    timer.start()
    system.start()












def demo():
    while True:
        print "CLI Interface test, select an option"
        print "1. Test Temperature"
        print "2. Test Timer"
        name = raw_input("Select an option ")
        if name == "1":
            sensorTest()
        elif name == "2":
            TimerTest()







    
def TimerTest():
    T = IncubatorTimer(0,21,0,0)
    while True:
       print T.getTimeRemaining()
def eggTrackerTest():
    e = eggBatch()
    e.addEgg("Silver - Laced - Wyanodotte")
    e.addEgg("Gold - Laced - Wyanodotte")
    e.addEgg("Black - Wyanodotte")
    e.printEggList()
    return 0

def sensorTest():
    s = Sensor()
    farenheit = temperatureUnits.FARENHEIT
    celsius = temperatureUnits.CELSIUS
    kelvin = temperatureUnits.KELVIN
    print 'Farenheit'
    s.setTemperatureUnit(farenheit)
    print s.getTemperature()
    print 'Celsius'
    s.setTemperatureUnit(celsius)
    print s.getTemperature()
    print 'Kelvin'
    s.setTemperatureUnit(kelvin)
    print s.getTemperature()
    print 'nonsense'
    s.setTemperatureUnit(99)
    print s.getTemperature()
    print 'Humidity'
    s.getHumidity()
if __name__ == "__main__":
    main()