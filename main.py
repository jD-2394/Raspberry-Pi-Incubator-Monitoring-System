from sensor import Sensor
from sensor import temperatureUnits
from Timer import IncubatorTimer
from eggTracker import eggBatch
def main():
    #sensorTest()
    #TimerTest()
    eggTrackerTest()
    
def TimerTest():
    T = IncubatorTimer(0,0,0,30)
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