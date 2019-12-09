from datetime import datetime, timedelta
class rateGeneratorController:
    def __init__(self, entry, exit):
        self.entry = entry
        self.exit = exit
        self.rateGenObj = rateGenerator(entry, exit)


    def isValid(self):
        if datetime.strptime(self.entry, '%Y-%m-%d %H:%M:%S.%f') < datetime.strptime(self.exit, '%Y-%m-%d %H:%M:%S.%f'):
            return True
        else:
            return False

    def calculatePayment(self):
        if (self.rateGenObj.isElegibleOneHour()):
            return(dict([('Rate', 'One Hour'),('Price', str(self.rateGenObj.calculateOneHourRate()))]))
        elif (self.rateGenObj.isElegibleNightRate()):
            return(dict([('Rate', 'Night Rate'),('Price', str(self.rateGenObj.calculateNightRate()))]))
        elif (self.rateGenObj.isElegibleTwoHour()):
            return(dict([('Rate', 'Two Hour'),('Price', str(self.rateGenObj.calculateTwoHourRate()))]))
        elif (self.rateGenObj.isElegibleWeekendRate()):
            return(dict([('Rate', 'Weekend Rate'),('Price', str(self.rateGenObj.calculateWeekendRate()))]))
        elif (self.rateGenObj.isElegibleEarlyBird()):
            return(dict([('Rate', 'Early Bird'),('Price', str(self.rateGenObj.calculateEarlyBirdRate()))]))
        elif (self.rateGenObj.isElegibleThreeHour()):
            return(dict([('Rate', 'Three Hour'),('Price', str(self.rateGenObj.calculateThreeHourRate()))]))
        else:
            return(dict([('Rate', 'Day Rate'),('Price', str(self.rateGenObj.calculateDayRate()))]))

class rateGenerator:
    def __init__(self, entry, exit):
        self.entry = datetime.strptime(entry, '%Y-%m-%d %H:%M:%S.%f')
        self.exit = datetime.strptime(exit, '%Y-%m-%d %H:%M:%S.%f')
        self.diff = self.exit - self.entry
        
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
        
    def calculateEarlyBirdRate(self):
        return self.earlybirdrate
    
    def isElegibleThreeHour(self):
        if self.diff.total_seconds() < 10800:
            return True
        else:
            return False
        
    def calculateThreeHourRate(self):
        return self.hourlyrate * 3
    
    def calculateDayRate(self):
        temp = (self.exit.date() - self.entry.date())
        temp = temp.days
        return self.dayrate * (temp + 1)