'''
Created on Feb 27, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''

'''
Memoization

0) Create a nested helper function that does the work. Pass an empty dictionary as a parameter

1) Check if the key is in the memo. If so, return the value associated with the key.

2) Use recursion to do work, but put the result in the local variable

3) Store the result in the memo and return the result
'''
import time

def fib(n):
    '''Returns the nth Fibonacci number.'''
    #tree recursion
    if n <= 1: #could also have two base cases where one could be n == 0 and another could be n == 1
        return n
    return fib(n-2) +fib(n-1)

def fib_memo(n):
    def fib_memo_helper(n,memo):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            result = n
        
        else:
            result = fib_memo_helper(n-1, memo) + fib_memo_helper(n - 2, memo)
        
        memo[n] = result
        return result
    
    return fib_memo_helper(n, {})

#start_time = time.time()
#print(fib(36))
#print(f'Computation time without memoization: {(time.time() - start_time) * 1000}')

#start_time = time.time()
#print(fib_memo(36))
#print(f'Computation time with memoization: {(time.time() - start_time) * 1000}')

def LCS(s1,s2):
    '''Returns the length of the longest common subsequence'''
    if not s1 or not s2:
        return 0
    elif s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    use_it = LCS(s1[1:], s2)
    lose_it = LCS(s1, s2[1:])
    return max(use_it,lose_it)

def LCS_memo(s1,s2):
    '''Returns the length of the longest common subsequence'''
    def LCS_memo_helper(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1,s2)]
        
        elif not s1 or not s2:
            result = 0
        
        elif s1[0] == s2[0]:
            #memo[(s1[1:], s2[1:])] = 1 + LCS_memo_helper(s1[1:], s2[1:],memo)
            result = 1 + LCS_memo_helper(s1[1:], s2[1:],memo)
        else:
            use_it = LCS_memo_helper(s1[1:], s2,memo)
            lose_it = LCS_memo_helper(s1, s2[1:],memo)
            result = max(use_it,lose_it)
        memo[(s1,s2)] = result
        return result
        
        
    return LCS_memo_helper(s1,s2,{})

#start_time = time.time()
#print(LCS('photosynthesis', 'dictionary'))
#print(f'Computation time without memoization: {(time.time() - start_time) * 1000}')

#start_time = time.time()
#print(LCS_memo('photosynthesis', 'dictionary'))
#print(f'Computation time without memoization: {(time.time() - start_time) * 1000}')

def LCS_with_values(s1,s2):
    '''Returns a tuple with the length of the longest common subsequence in
    strings s1 and s2 as well as the LCS itself'''
    if not s1 or not s2:
        return (0,'')
    
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return (1 + result[0], s1[0] + result[1])
    
    use_s1 = LCS_with_values(s1, s2[1:])
    use_s2 = LCS_with_values(s1[1:], s2)
    
    if use_s1[0] > use_s2[0]:
        return use_s1
    
    return use_s2

def LCS_with_values_memo(s1,s2):
    '''Returns a tuple with the length of the longest common subsequence in
    strings s1 and s2 as well as the LCS itself'''
    def LCS_with_values_memo_helper(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1,s2)]
        
        if not s1 or not s2:
            result = (0,'')
        
        elif s1[0] == s2[0]:
            lose_both = LCS_with_values_memo_helper(s1[1:], s2[1:], memo)
            result = (1 + lose_both[0], s1[0] + lose_both[1])
        
        else:
            use_s1 = LCS_with_values_memo_helper(s1, s2[1:], memo)
            use_s2 = LCS_with_values_memo_helper(s1[1:], s2, memo)
    
            if use_s1[0] > use_s2[0]:
               result = use_s1
            
            else:
                result = use_s2
        
        memo[(s1,s2)] = result
        return result

    return LCS_with_values_memo_helper(s1,s2, {})

start_time = time.time()
print(LCS_with_values('photosynthesis', 'dictionary'))
print(f'Computation time without memoization: {(time.time() - start_time) * 1000}')

start_time = time.time()
print( LCS_with_values_memo('photosynthesis', 'dictionary'))
print(f'Computation time without memoization: {(time.time() - start_time) * 1000}')