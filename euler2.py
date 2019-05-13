'''
Created on May 6, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
v = 0
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(1)) 
 
n = 2 #because the fib sequence in problem starts at the n = 2 term
v = 0

while True:
    term = fibonacci(n)
    if term < 4000000:
        if term % 2 == 0:
            v += fibonacci(n)
        n += 1
    else:
        break
print(v)


#Alternative way
LIMIT = 4000000
a = 1
b = 2
sum_even = 0
while b <= LIMIT:
    if b % 2 == 0:
        sum_even += b
    
    c = b
    b += a
    a = c
print(sum_even)