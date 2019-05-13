'''
Created on Mar 23, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
def numToBaseB(N,B):
    '''convert from decimal to whichever base the user wishes'''
    def helper(n,b):
        if n == 0:
            return ''
        else:
            return helper(n//b, b) + str(n%b)
    if N == 0:
        return '0'
    else:
        return helper(N, B)
#print(numToBaseB(4, 2))
#print(numToBaseB(4, 3))
#print(numToBaseB(4, 4))
#print(numToBaseB(0, 4))
#print(numToBaseB(0, 2))
def baseBToNum(S, B):
    '''converts back to decimal'''
    def helper(s,b):
        if s == '':
            return 0
        else:
            return (b ** (len(s)-1))*int(s[0]) + baseBToNum(s[1:],b)
    if S == '0':
        return 0
    else:
        return helper(S, B)
#print(baseBToNum("11", 2))
#print(baseBToNum("11", 3))
#print(baseBToNum("11", 10))
#print(baseBToNum("", 10))
def baseToBase(B1,B2,SinB1):
    ''' takes three inputs: a base B1, a base B2 (both of which are
between 2 and 10, inclusive) and SinB1, which is a string representing a number in
base B1. baseToBase should return a string representing the same number in base B2.'''
    decimal_value = baseBToNum(SinB1, B1)
    return numToBaseB(decimal_value, B2)
#print( baseToBase(2, 10, "11") )
#print( baseToBase(10, 2, "3") )
#print(baseToBase(3, 5, "11"))
def add(S,T):
    '''takes
two binary strings S and T as input and returns their sum, also in binary. '''
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2),2)
#print(add("11", "01"))
#print(add("011", "100"))
#print(add("110", "011"))
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
print(addB("11", "1"))
print(addB("011", "100"))
print(addB('0','0'))
print(addB('',''))
print(addB('11',''))


