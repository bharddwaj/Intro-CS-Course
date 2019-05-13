'''
Created on January 30, 2019

I pledge my honor that I have abided by the Stevens Honor System.

@author: Bharddwaj Vemulapalli
Username: bvemulap

'''

from cs115 import map,reduce

def span(lst):
    '''Returns the difference between the maximum and minimum numbers in a List.'''
    return reduce(max,lst) - reduce(min, lst)

print(span([3,1,42,7]))

def gauss(N):
    '''Takes as input the positive integer N and returns
    the sum 1 + 2 + ... + n'''
    return reduce(lambda x,y: x+y,range(1,N+1))

print(gauss(100))

def sum_of_squares(N):
    '''Takes as input a positive integer n and returns the sum
    1^2 + 2^2 + ... + n^2 '''
    return reduce(lambda x,y: x + y,map(lambda x: x*x,range(1,N+1)))

print(sum_of_squares(100))

list_of_strings = ['hello',', ','my','name','is','Bharddwaj','.']
print(map(len,list_of_strings))

list_of_ints = [1,2,3,4,5]
print(reduce(lambda x,y: x*y, list_of_ints))