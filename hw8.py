'''
Created on Mar 31, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from functools import reduce
''' Helper Functions '''
FullAdder ={ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }
def addB(s1,s2):
    ''' function should return a new string representing the sum of the two input strings. The sum
needs to be computed using the binary addition algorithm, shown above, and not using base conversions.'''
    '''function also assumes '' is 0'''
    if len(s1) < 8:
        s1 = '0'*(8-len(s1)) + s1
    if len(s2) < 8:
        s2 = '0'*(8-len(s2)) + s2
    
    def helper(S1,S2,carry):
        if not S1 and not S2:
            return '' 
        sum = FullAdder[(S1[len(S1)-1],S2[len(S2)-1],carry)]
        #print(sum)
        #could've done sumBit, carryBit = FullAdder[('0','0','1')] instead
        return helper(S1[0:len(S1)-1], S2[0:len(S2)-1], sum[1]) + sum[0]
    function_call = helper(s1, s2, '0')
    if '1' in function_call:
        eliminate_zero = function_call.index('1')
        return function_call[eliminate_zero:]
    else:
        #means ans is zero or null
        return function_call[-1]
    
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
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n == 1:
        return '1'
    if n%2 != 0:
        return numToBinary(n//2) + f'{n % 2}' 
    else:
        return numToBinary(n//2) + '0' 
''' ''' ''' ''' ''' '''
def TcToNum(s):
    '''takes as input a string of 8 bits representing an integer in two's-complement, and returns the corresponding integer.'''
    if s[0] == '0':
        return binaryToNum(s)
    else:
        complement = reduce(lambda x,y: x + y,list(map(lambda x: '1' if x == '0' else '0',s)))
        
        return -1*binaryToNum(addB(complement, '00000001'))

#print(TcToNum("00000001"))
#print(TcToNum("11111111"))
#print(TcToNum("10000000"))
#print(TcToNum("01000000"))

def NumToTc(N):
    '''takes as input an integer N, and returns a string representing the two's-complement representation of that integer.'''
    if -128 <= N < 0:
        conversion = numToBinary(-1*N)
        if len(conversion) < 8:
            conversion = '0'*(8-len(conversion)) + conversion
        complement = reduce(lambda x,y: x + y,list(map(lambda x: '1' if x == '0' else '0',conversion)))
        return addB(complement, '00000001')
    elif 0 <= N < 128:
        conversion = numToBinary(N)
        if len(conversion) < 8:
            conversion = '0'*(8-len(conversion)) + conversion
        return conversion
    else:
        return 'Error'

#print(NumToTc(1)) 
#print(NumToTc(-128))     
#print(NumToTc(200))
        
        
    
    
    
    
    
    