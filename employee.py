'''
CS 115, Inheritance Activity

Author: Bharddwaj Vemulapalli
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RULES: You can use Canvas to download this file and upload your solution.
' You can use Eclipse to edit and run your program. You should NOT look at
' other programs in Eclipse, you should NOT use any other programs, and you
' should NOT use any notes or books.
' According to the Honor Code, you should report any student who appears
' to be violating these rules.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 7 (15 points)
' Implement missing sections of the Employee class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Employee(object):
    '''Write the constructor below. It should take in five arguments:
       - first_name (a string)
       - last_name (a string)
       - title (a string)
       - hours_per_week (an int)
       - hourly_rate (a float)
       All fields must be private. No error checking or type conversions
       are required.
       5 points'''
    def __init__(self,first_name,last_name,title,hours_per_week,hourly_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__title = title
        self.__hours_per_week = hours_per_week
        self.__hourly_rate = hourly_rate

    '''Write a property for hourly_rate. 3 points'''
    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def title(self):
        return self.__title
    @property
    def hours_per_week(self):
        return self.__hours_per_week
    @property
    def hourly_rate(self):
        return self.__hourly_rate

    '''Write a setter for hourly rate. 3 points'''
    @first_name.setter
    def first_name(self,first_name):
        self.__first_name = first_name
    @last_name.setter
    def last_name(self,last_name):
        self.__last_name = last_name
    @title.setter
    def title(self,title):
        self.__title = title
    @hours_per_week.setter
    def hours_per_week(self,hours_per_week):
        self.__hours_per_week = hours_per_week
    @hourly_rate.setter
    def hourly_rate(self,hourly_rate):
        self.__hourly_rate = hourly_rate
        
    def get_total_compensation(self):
        '''Write a method called get_total_compensation.
       It returns the total amount of money an employee earns in a year.
       Assume that the employee works 50 weeks each year, with the remaining
       2 set aside for vacation.
       4 points'''
        return 50*self.__hours_per_week*self.__hourly_rate

    def __str__(self):
        return 'Employee: %s %s\n  Title: %s\n  Hours per week: %d\n' \
               '  Hourly rate: $%.2f\n  Yearly compensation: $%.2f' % \
            (self.__first_name, self.__last_name, self.__title, \
             self.__hours_per_week, self.__hourly_rate, \
             self.get_total_compensation())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (15 points)
' Implement missing sections of the Manager class. Manager should be a
' subclass of Employee.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Manager(Employee):  # 2 points
    '''Write the constructor below. It should take in six arguments:
    - the first five are the same as in the Employee constructor
    - bonus_percent, a float >= 0. This attribute represents the percentage
      of the employee's yearly compensation that will be used to
      create the manager's annual bonus. MAKE SURE the argument is a float
      >= 0.  Otherwise, if it's not a float raise a TypeError stating,
      "Bonus percent must be a float." If it's a float but < 0, raise a
      ValueError stating, "Bonus percent cannot be negative."
      bonus_percent must be private.
    8 points'''
    def __init__(self, first_name, last_name, title, hours_per_week, hourly_rate,bonus_percent):
        super().__init__(first_name, last_name, title, hours_per_week, hourly_rate)
        #that is constructor chaining
        try:
            bonus_percent = float(bonus_percent)
        except:
            #starts out as a valueerror but u make it a typeerror
            raise TypeError("Bonus percent must be a float.")
        
        if bonus_percent < 0.0:
            raise ValueError( "Bonus percent cannot be negative.")
        self.__bonus_percent = bonus_percent
        

    '''Override the method get_total_compensation.
    It returns the total amount of money the manager earns in a year, i.e.
    basic employee compensation + bonus.
    To get full credit, you must call get_total_compensation in the superclass.
    Note: If a manager's yearly compensation is $100,000 and the bonus_percent
          is 10 (ten), the total compensation will be 110,000.
    5 points'''
    def get_total_compensation(self):
        return super().get_total_compensation()*(1+self.__bonus_percent*.01)

if __name__ == '__main__':
    e1 = Employee('Bharddwaj','Vemulapalli','Quant',40,30)
    print(e1)
    e1.hourly_rate = 40
    print(e1.hourly_rate)
    print(e1)
    m = Manager('Bron','James','Basketball Phenom',40,30,100)
    print(m)
    m.hourly_rate = 40
    print(m.hourly_rate)
    print(m)
    