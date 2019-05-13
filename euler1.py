'''
Created on May 6, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''
import sys
sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

def mul_3_5(i,sum):
    if i == 1000:
        return sum
    elif i % 3 == 0:
        
        sum += i
        i += 1
        return mul_3_5(i, sum)
    elif i % 5 == 0:
        sum += i
        i += 1
        return mul_3_5(i, sum)
    else:
        i += 1
        return mul_3_5(i, sum)

sum = 0
i = 0  
sys.setrecursionlimit(1001)
print(mul_3_5(i, sum))
    
        