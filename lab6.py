'''
Created on March 6th, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Lab 6
'''
from builtins import len
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    #true if odd
    return n % 2 != 0
    #1. 101010
    #2. If the number is odd, the right most bit will be 1 because that's the only way you can get an odd number in binary.
    #    If you are given an even number the least significant number will be 0 because if 1 makes the base 2 odd, the 0 makes it even
    #3  If you remove the last digit then you are essentially performing floor division by 2.
    #4 If N is an odd number you would add a 1 onto the end of the binary sequence whereas if it was even you would add a 0.
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n == 1:
        return '1'
    if isOdd(n):
        return numToBinary(n//2) + f'{n % 2}' 
    else:
        return numToBinary(n//2) + '0' 
    

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s == '1':
        return 1
    elif s[0] == '1':
        return 2 ** (len(s)-1) + binaryToNum(s[1:])
    else:
        #if s[0] == '0'
        return binaryToNum(s[1:])
        

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    else:
        #function_call = numToBinary(binaryToNum(str(int(s) + 1)))
        function_call = numToBinary(binaryToNum(s) + 1)
        difference = 8 - len(function_call)
        return '0'*difference + function_call

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else:
        starting_number = binaryToNum(s)
        list_of_increments = [s] + list( map(increment,map(numToBinary, range(starting_number,starting_number + n) ) ))
        print(list_of_increments)
        
# count('00000000',4)
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n == 1:
        return '1'
    elif n%3 != 0:
        return numToTernary(n//3) + f'{n % 3}'
    else:
        return numToTernary(n//3) + '0'
        
        

#5. 59 is 2012 in ternary (2*(3^0) + 1 * 3^1 + 2 * 3^3) = 59
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return (3 ** (len(s)-1))*int(s[0]) + ternaryToNum(s[1:])
    

# print(numToBinary(294))
# print(binaryToNum(numToBinary(294)))
# print(increment(numToBinary(294)))
# print(count(numToBinary(294), 3))
# print(list(map(binaryToNum,count(numToBinary(294), 3))))