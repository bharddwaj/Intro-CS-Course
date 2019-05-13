'''
Created on 4/20
@author:   Bharddwaj Vemulapalli
username: bvemulap
Pledge:   I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and \
           self.day == d2.day
    
    def tomorrow(self):
        '''change the calling object so that it represents one calendar day 
        after the date it originally represented.'''
        if self.day == 31 and self.month != 12:
            self.day = 1
            self.month += 1
        elif self.day == 31 and self.month == 12:
            self.day = 1
            self.month = 1 
            self.year += 1   
        elif self.day == 28 and self.month == 2:
            if self.isLeapYear():
                self.day = 29
            else:
                self.day = 1
                self.month = 3
        elif self.day == 29 and self.month == 2:
            self.day = 1
            self.month = 3
        
        elif self.day == 30 and self.month in [4,6,9,11]:
            self.day = 1
            self.month += 1
        else:
            self.day += 1
    
    def addNDays(self, N):
        '''changes the date to N days forward in time by repeatedly calling the tomorrow method'''
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)
    
    def subNDays(self, N):
        '''changes the date to N days backward in time by repeatedly calling the yesterday method'''
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)
            
    def yesterday(self):
        '''change the calling object so that it represents one calendar day 
        before the date it originally represented.'''

        if self.day == 1 and self.month == 1:
            self.day = 31
            self.month = 12 
            self.year -= 1 
        
        elif self.day == 1 and self.month == 3:
            self.month = 2
            if self.isLeapYear():
                self.day = 29
                
            else:
                self.day = 28
                
        elif self.day == 1 and self.month in [5,7,10,12]: #used to be in instead of not in
            self.day = 30
            self.month -=1
        elif self.day == 1:
            self.day = 31
            self.month -= 1
        
        else:
            self.day -= 1
            
    def isBefore(self, d2):
        '''outputs whether the date is before that of the inputed object's date'''
        if self.year < d2.year:
            return True
        
        elif self.month < d2.month and d2.year == self.year:
            return True
        elif self.day < d2.day and self.month == d2.month and d2.year == self.year:
            return True
        else:
            return False
    
    def isAfter(self,d2):
        '''outputs whether the date is after that of the inputed object's date'''
        return not self.isBefore(d2) and not self.equals(d2)
    
    def diff(self, d2):
        ''' return the difference between the inputed object's date and this object's date'''
        copy_o = self.copy()
        
        if self.equals(d2):
            return 0
        elif self.isBefore(d2):
            #print("Self is before d2")
            count = 0
            while copy_o.isBefore(d2):
                count+=1
                copy_o.tomorrow()
                #print(copy_o)
                
            return -1*(count)
        else:
            #print("Self is after d2")
            count = 0
            while copy_o.isAfter(d2):
                count+=1
                copy_o.yesterday()
                #print(copy_o)
            return count
        
    def dow(self):
        '''return a string that indicates the day of the week (dow) of the object (of type Date) that calls it.'''
        # http://mathforum.org/dr.math/faq/faq.calendar.html
        # Key Value method
        month_codes = {1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
        century_codes = {17:4,18:2,19:0,20:6}
        week_codes = {0:'Saturday',1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday'}
        obj = self.copy()
        new_obj_year = obj.year
        #obj.year//100 != 20 or obj.year//100 != 19 or obj.year//100 != 18 or obj.year//100 != 17
        
        while new_obj_year//100 != 20 and new_obj_year//100 != 19 and new_obj_year//100 != 18 and new_obj_year//100 != 17:
            new_obj_year = new_obj_year - 400
            
        
        if self.isLeapYear() and (obj.month == 1 or obj.month == 2):
            return week_codes[((obj.year%100)//4 + obj.day +month_codes[obj.month] - 1 + century_codes[new_obj_year//100] + new_obj_year%100)%7]
        else:
            return week_codes[((obj.year%100)//4 + obj.day +month_codes[obj.month] + century_codes[new_obj_year//100] + new_obj_year%100)%7]


