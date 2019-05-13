'''
Created on Jan 31, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import map,reduce

def mult(x, y):   
    """Returns the product of x and y"""
    return x * y

def factorial(n):
    '''takes in an argument n and returns n!'''
    return reduce(mult,range(1,n+1))

def add(x,y):
    '''returns the sum of two arguments it takes in'''
    return x + y 

def mean(lst):
    '''returns the average of the list by adding all the terms and dividing
    by the number of elements in the list'''
    return reduce(add,lst)/len(lst)

def divides(n):
    '''takes in argument n and k and checks to see whether there is any remainder '''
    def div(k):
      return  n % k == 0
    return div

def prime(n):
    '''takes argument n and checks whether the number is prime'''
    #first map applies the divides function which checks if n is divisible by any number excluding itself and 1
    #second map typecasts all the booleans to be string so I can apply len
    #third map applies the len() function to each string(boolean)
    #using reduce I add up all of the lengths
    #then I check whether they add up to 5*the length of the whole range itself, this means that n is not divisible by any number
    #since the above method doesn't work for 2 i just added an or statement
    if n < 2:
        return False
    return n == 2 or reduce(add,map(len,map(str,map(divides(n),range(2,n))))) == 5*len(range(2,n))

def prime2(n):
    if n<=1:
        return False
    return reduce(add,map(divides(n),range(1,n)))== 1

def prime3(n):
    if n < 2:
        return False
   
    return sum(map(divides(n),range(2,n))) == 0

