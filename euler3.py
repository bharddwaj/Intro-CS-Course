'''
Created on May 6, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
#factors start repeating after the square root
from math import sqrt

def euler3(n):
    factors = []
    i = 2
    while True:
        maxfactor = int(sqrt(n))
        if i <= maxfactor:
            if n % i == 0:
                n //= i
                factors.append(i)
            else:
                i += 1
        else:
            factors.append(n)
            break
    print(factors)
    return max(factors)

print(euler3(600851475143))
        