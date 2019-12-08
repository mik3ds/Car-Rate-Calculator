#Assuming input as YYYY-MM-DD hh:mm:ss, e.g. 2019-12-06 12:30:00PM

from datetime import datetime, timedelta

class Main:
    def __init__(self, entryS, exitS):
        entry = datetime.strptime(entryS, '%Y-%m-%d %H:%M:%S.%f')
        exit = datetime.strptime(exitS, '%Y-%m-%d %H:%M:%S.%f')
        diff = exit - entry

        #add validation here
        g = rateGenerator(entry,exit)
        


    
class rateGenerator:
    def __init__(self, entry, exit):
        self.entry = entry
        self.exit = exit
        self.diff = exit - entry
        
        self.weekdays = [0,1,2,3,4]
        self.weekends = [5,6]
        
        self.hourlyrate = 5
        self.dayrate = 20

        self.earlybirdrate = 13
        self.nightrate = 6.5
        self.weekendrate = 10
        
        self.earlybirdenterstart = 6
        self.earlybirdenterend = 9
        self.earlybirdexitstart = 15.5
        self.earlybirdexitend = 24

        self.nightrateenterstart = [18,0]
        self.nightrateenterend = [0,0]
        self.nightrateexitstart = [15,30]
        self.nightrateexitend = [23,30]
        
    def isElegibleOneHour(self):
        if self.diff.total_seconds() < 3600:
            return True
        else:
            return False
    
    def calculateOneHourRate(self):
        return self.hourlyrate
    
    def isElegibleNightRate(self):
        #create date objects for targets
        self.nightRateEnterStartDate = self.entry.replace(hour=self.nightrateenterstart[0], minute=self.nightrateenterstart[1])
        self.nightRateEnterEndDate = self.entry.replace(hour=self.nightrateenterend[0], minute=self.nightrateenterend[1])
        self.nightRateExitStartDate = self.entry.replace(hour=self.nightrateexitstart[0], minute=self.nightrateexitstart[1])
        self.nightRateExitEndDate = self.entry.replace(hour=self.nightrateexitend[0], minute=self.nightrateexitend[1])
        #validation for values ending midnight
        if self.nightRateEnterStartDate > self.nightRateEnterEndDate:
            self.nightRateEnterEndDate += timedelta(days=1)
        if self.nightRateExitStartDate > self.nightRateExitEndDate:
            self.nightRateExitEndDate += timedelta(days=1)
        if self.nightRateEnterEndDate > self.nightRateExitStartDate:
            self.nightRateExitStartDate += timedelta(days=1)
            self.nightRateExitEndDate += timedelta(days=1)
        if (self.entry.weekday() in self.weekdays and 
        self.diff.days in [0,1] and 
        (self.nightRateEnterStartDate <= self.entry < (self.nightRateEnterEndDate)) and 
        (self.nightRateExitStartDate <= self.exit < self.nightRateExitEndDate)):
            return True
        else:
            return False

    def calculateNightRate(self):
        return self.nightrate

    def isElegibleTwoHour(self):
        if self.diff.total_seconds() < 7200:
            return True
        else:
            return False
        
    def calculateTwoHourRate(self):
        return self.hourlyrate * 2

    def isElegibleWeekendRate(self):
        if (self.entry.weekday() in self.weekends and 
        self.exit.weekday() in self.weekends and 
        self.diff.days in [0,1]):
            return True
        else:
            return False

    def calculateWeekendRate(self):
        return self.weekendrate

    def isElegibleEarlyBird(self):
        if ((self.entry.date() == self.exit.date()) and 
        (self.earlybirdenterstart <= self.entry.hour < self.earlybirdenterend) and 
        (self.earlybirdexitstart <= self.exit.hour < self.earlybirdexitend)):
            return True
        else:
            return False
        
    def calculateEarlyBird(self):
        return self.earlybirdrate
    
    def isElegibleThreeHour(self):
        if self.diff.total_seconds() < 10800:
            return True
        else:
            return False
        
    def calculateThreeHourRate(self):
        return self.hourlyrate * 3
    
    def calculateDayRate(self):
        return self.dayrate * (self.diff.days + 1)
    

entryS = '2019-12-06 18:01:00.000000'
exitS = '2019-12-07 15:31:00.000000'

a = datetime.strptime(entryS, '%Y-%m-%d %H:%M:%S.%f')
b = datetime.strptime(exitS, '%Y-%m-%d %H:%M:%S.%f')
g = rateGenerator(a,b)


if (g.isElegibleOneHour()):
    print('One Hour ')
    print(g.calculateOneHourRate())
elif (g.isElegibleNightRate()):
    print('Night Rate ')
    print(g.calculateNightRate())
elif (g.isElegibleTwoHour()):
    print('Two Hour ')
    print(g.calculateTwoHourRate())
elif (g.isElegibleWeekendRate()):
    print('Weekend Rate')
    print(g.calculateWeekendRate())
elif (g.isElegibleEarlyBird()):
    print('Early Bird')
    print(g.calculateEarlyBird())
elif (g.isElegibleThreeHour()):
    print('Three Hour')
    print(g.calculateThreeHourRate())
else:
    print('Day Rate ' + str(g.calculateDayRate()))
