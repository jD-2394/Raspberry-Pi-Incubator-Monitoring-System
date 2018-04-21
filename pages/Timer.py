import datetime
import time
import sys
class IncubatorTimer:
    
    def __init__(self,d=0,h=0,m=0,s=0):
        self.days = d
        self.hours = h
        self.minutes = m
        self.seconds = s
        self.futureTime = datetime.timedelta(days = self.days, hours = self.hours, minutes = self.minutes, seconds = self.seconds ) + datetime.datetime.now()
    def getTimeRemaining(self):
            time_duration = self.futureTime - datetime.datetime.now()
            days, seconds = time_duration.days, time_duration.seconds
            hours = days * 24 + seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            return days , ':' , hours , ':' , minutes , ':' , seconds
            #return time()