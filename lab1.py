'''
Created on January 30, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import map,reduce
import math
def dbl(x):     
    """Returns twice its input x        
    input x: a number (int or float)""" 
    return 2 * x

def inverse(n):
    ''' Takes a number, n, as input and returns its reciprocal. '''
    return float('%.17f' % (1/n)) #least amount of digits it takes to get the 1 at the end of all those 3s

def e(n):
    '''approximates the mathematical value e using a Taylor expansion.'''
    list_of_numbers = range(1,n+1)
    def add (x,y): 
        return x + y
    return float(1 + reduce(add,map(inverse,map(math.factorial, list_of_numbers))))

def error(n):
    '''returns the absolute value of the difference between the "actual" value of e ''' 
    return abs(math.e-e(n))

