'''
Created on Feb 20, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import map, reduce
''' Helper Function '''
def factorial(n):
    '''Computes n factorial'''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) #pending operation
''' ''' ''' ''' ''' ''' ''' ''' ''' '''
    
#combinations formula: n!/[k! * (n-k)!]
def pascal_row(row_number):
    '''Returns a list of elements found in a certain row of Pascal’s Triangle.'''
    if row_number == 0:
        return [1]
    if row_number == 1:
        return [1] + pascal_row(row_number - 1)
    
    def secondary_helper(k): 
        #iterates from k = 0 to k = row_number in order to get all the numbers in that row
        if k != row_number:
            return [int(factorial(row_number)/(factorial(k) * factorial(row_number - k)))] + secondary_helper(k + 1)
        return [int(factorial(row_number)/(factorial(k) * factorial(row_number - k)))]
    
    return secondary_helper(0)

#print(pascal_row(0))
#print(pascal_row(1))
#print(pascal_row(5))

def pascal_triangle(n):
    '''takes as input a single integer n and returns a list of lists containing the values of the all the rows up to and including row n.'''
    if n == 0:
        return [pascal_row(0)]
    return   pascal_triangle(n - 1) + [pascal_row(n)]

#print(pascal_triangle(0))
#print(pascal_triangle(1))
#print(pascal_triangle(5))