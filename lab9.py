'''
Created on Apr 3, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''

def mult( c, n ):
    """ mult uses only a loop and addition
    to multiply c by the integer n
    """
    result = 0
    for x in range( n ):
        # update the value of result here in the loop
        result += c
    return result
#print(mult(6, 7))
def update( c, n ):
    """ update starts with z=0 and runs z = z**2 + c
    for a total of n times. It returns the final z.
    """
    z = 0
    for x in range(n):
        z = z**2 + c
    return z
#print(update( 1, 3 ))
#print(update( -1, 3 ))
#print(update( 1, 10 ))
#print(update( -1, 10 ))
def inMSet(c, n):
    """ inMSet takes in
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
        Then, it should return
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True #abs(z) <= 2 this still worked though
c = 0 + 0j
print(inMSet(c, 25))  
c = 3 + 4j
print(inMSet(c, 25))
c=0.3+-0.5j
print(inMSet(c, 25))
c=-0.7+0.3j
print(inMSet(c, 25))
c = 0.42 + 0.2j
print(inMSet(c, 25))
print(inMSet(c, 50))
