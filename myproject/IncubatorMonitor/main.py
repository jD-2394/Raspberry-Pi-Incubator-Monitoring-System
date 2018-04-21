from sensor import Sensor
from sensor import temperatureUnits
from eggTracker import *
from interface import *
import thread
import datetime
import sched,time
import numbers
#from stream import ClimateThread
import threading
from random import *
from threading import *
import time
current_temperature = 0
current_humidity = 0

curSysInterface = systemInterface()




def main():
    print("Test Sensor")
    curSensor = Sensor()
    print(curSensor.getTemperature())
    print(curSensor.getHumidity())

    print(curSensor.getTemperature())
    print(curSensor.getHumidity())

    print(curSensor.getTemperature())
    print(curSensor.getHumidity())
    print("Test Climate Thread..")
    climateThread = ClimateThread()
    climateThread.start()

    print(curSensor.getTemperature())
    print(curSensor.getHumidity())

    print(curSensor.getTemperature())
    print(curSensor.getHumidity())

    print(curSensor.getTemperature())
    print(curSensor.getHumidity())

    print("Test system interface using thread...")
    print(curSysInterface.getTemperature())
    print(curSysInterface.getHumidity())

    print(curSysInterface.getTemperature())
    print(curSysInterface.getHumidity())

    print(curSysInterface.getTemperature())
    print(curSysInterface.getHumidity())

if __name__ == "__main__":
    main()