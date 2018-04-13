from interface import systemInterface
import thread
from random import *
from threading import *
import time

class ClimateThread(Thread):
    def __init__(self):
        self.humidity = 0
        self.temperature = 0
        self.running = False
        self.m = Lock()
        super(Thread, self).__init__()

    def start(self):
        self.running = True

    def getTemperature(self):
        m.acquire()
        s = self.temperature
        m.release()
        return s
    def getHumidity(self):
        m.acquire()
        s = self.humidity
        m.release()
        return s


    def run(self):
        while self.running:
            m.acquire()
            self.humidity = randint(1,100) #placeholder for sensor input
            m.release()
            m.acquire()
            self.temperature = randint(1,100)  #placeholder for sensor input
            m.release()
            print(self.getTemperature())
            print(self.getHumidity())
            time.sleep(1) # wait a second
