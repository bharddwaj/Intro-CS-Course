'''
Created on Feb 4, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import map,reduce,filter
import math


def factorial(n):
    '''Computes n factorial'''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) #pending operation

print(f'Factorial: {factorial(70)}')

def tower(n):
    '''raises 2 to that power n-1 times'''
    if n == 0:
        return 1
    
    else:
        return 2** tower(n - 1)
print(map(tower,range(6)))

def length(lst):
    '''Returns the length of the list'''
    if not lst:
        return 0
    else:
        return 1 + length(lst[:-1])

print(length([0,1,2,3]))

def reverse(lst):
    '''takes as input a list of elements and returns the List in reverse order'''
    ''' Linear '''
    if length(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse(lst[:-1])
        #return reverse(lst[1:]) + [lst[0]]

def member(x,lst):
    '''returns true if x is contained in the list and false otherwise'''
    ''' Tail Recursion '''
    if not lst:
        return False
    
    elif x == lst[0]:
        return True
    
    else:
        return member(x, lst[1:])

print(member(2, [0,2]))
    
def collapse(lst):
    '''collapses a list of possibly nested lists into a single list of values'''
    #exmaple of tree recursion where the pending operation is another recursive call
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return collapse(lst[0])+ collapse(lst[1:])
    else:
        return [lst[0]] + collapse(lst[1:])

something = [1,[2,3],[4, [5,6]]]
print(collapse(something))
    
def my_map(f,lst):
    '''Returns a new list where the function f has been applied to every element in the original list'''
    if not lst:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def sqr(x):
    return x * x  
    
print(my_map(sqr, [0,1,2,3,4,5]))  

def tower_reduce(n):
    '''raises 2 to that power n-1 times'''
    def power(x,y):
        return y ** x
    return reduce(power,[2] * n)

print(tower(4))
print(tower_reduce(4))

def power(x,y):
    '''Computes x raised to the y using recursion'''
    if y == 0:
        return 1
    return x * power(x,y - 1)

print(power(4,3))

def power_tail(x,y):
    '''computes x raised to the y using tail recursion'''
    def power_tail_helper(x,y,accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y-1, x * accum)
    return power_tail_helper(x,y,1)

print(power_tail(4,3))
 
def my_reduce(f,lst):
    '''Reduces the list to a single value as dictated by the predicate f'''
    def my_reduce_helper(f,lst,accum):
        if not lst:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum,lst[0]))
    if not lst:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f,lst[1:],lst[0])
print(my_reduce(lambda x,y: x + y, [0,1,2,3,4]))

def prime(n):
    '''Returns whether or not an integer is prime.'''
    possible_divisors = range(2,int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0
print(prime(10))
print(prime(17))

def primes(n):
    '''Returns a list of primes in the range [2,n] inclusive computed via the sieve of Eratothenes'''
    def sieve(lst):
        if not lst:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0,lst[1:]))
    return sieve(range(2,n+1))

print(primes(354))

def fib(n):
    '''Returns the nth Fibonacci number.'''
    #tree recursion
    if n <= 1: #could also have two base cases where one could be n == 0 and another could be n == 1
        return n
    return fib(n-2) +fib(n-1)
print(map(fib,range(6)))  

  