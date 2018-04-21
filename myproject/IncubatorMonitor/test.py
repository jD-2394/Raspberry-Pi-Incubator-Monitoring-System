#!/usr/bin/python
from interface import systemInterface
import time

cur_interface = systemInterface()

def testEggTracker():
    cur_interface.addEggToBatch("Wyanodotte","Chicken","Medium")
    cur_interface.addEggToBatch("Buff Orphington", "Chicken", "Medium")
    cur_interface.addEggToBatch("Polish", "Chicken", "Small")
    cur_interface.addEggToBatch("Wyanodotte", "Chicken", "Medium")
    cur_interface.addEggToBatch("Leghorn", "Chicken", "Jumbo")

    cur_interface.printEggList()
    cur_interface.removeEgg(4)
    cur_interface.printEggList()

def testTimer():
    cur_interface.setHatchTime(24)
    cur_interface.startHatchTime()
    while True:
       print(cur_interface.getHatchTime())
       time.sleep(1)


def testClimate():
    cur_interface.getHumidity()
    cur_interface.setTemperatureUnits("Celsius")
    cur_interface.getTemperature()
    cur_interface.setTemperatureUnits("Farenheit")
    cur_interface.getTemperature()
    cur_interface.setTemperatureUnits("Kelvin")
    cur_interface.getTemperature()



def main():
    testTimer()


if __name__ == "__main__":
    main()