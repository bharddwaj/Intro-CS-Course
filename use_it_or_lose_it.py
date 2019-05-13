'''
Created on Feb 11, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import map

def powerset(lst):
    '''Returns the powerset of the list that is the set of all subsets of the list'''
    if not lst:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

#print(powerset([1,2,3]))

def subset(target,lst):
    '''Determines whether or not it is possible to create a target sum using
    the values in the list. Values in the list can be positive, negative, or zero'''
    if target == 0:
        return True
    elif not lst:
        return False
    '''
    use_it = subset(target-lst[0], lst[1:])
    lose_it = subset(target, lst[1:])
    return use_it or lose_it
    '''
    return subset(target-lst[0], lst[1:]) or subset(target, lst[1:])
#print(subset(7, [5,1,2]))

def LCS(s1,s2):
    '''Returns the length of the longest common subsequence'''
    if not s1 or not s2:
        return 0
    elif s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    use_it = LCS(s1[1:], s2)
    lose_it = LCS(s1, s2[1:])
    return max(use_it,lose_it)
#print(LCS('spot','poop'))
#print(LCS('happen','get'))

def subset_with_values(target,lst):
    '''Determines whether or not it is possible to create a target sum using
    the values in the list. Values in the list can be positive, negative, or zero.
    The function returns a tuple of exactly two items. The first is a boolean that
    indicates True if the sum is possible and False if its not. The second element
    in the tuple is a list of all the values that add up to make the target sum.'''
    if target == 0:
        return (True,[])
    elif not lst:
        return (False,[])
    use_it = subset_with_values(target-lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    #lose_it = subset_with_values(target, lst[1:])
    return subset_with_values(target, lst[1:])

#print(subset_with_values(7, [5,1,2]))

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

def coin_row(lst):
    '''goal is to pick up the maximum amount of money subject to the constraint that no two coins
     adjacent in the initial row can be picked up.'''
    if not lst:
        return 0
    #use_it = lst[0] + coin_row(lst[2:])
    #lose_it = coin_row(lst[1:])
    return max(lst[0] + coin_row(lst[2:]),coin_row(lst[1:]))

#print(coin_row([]))
#print(coin_row([5, 1, 2, 10, 6, 2]))
#print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def coin_row_with_values(lst):
    if not lst:
        return [0,[]]
    
    use_it_result = coin_row_with_values(lst[2:])
    lose_it_result = coin_row_with_values(lst[1:])
    
    use_it = [lst[0] + use_it_result[0], [lst[0]] + use_it_result[1]]
    #lose_it = [lose_it_result[0],lose_it_result[1]] #don't really need this line
    
    if use_it[0] > lose_it_result[0]:
        return use_it
    return lose_it_result

#print(coin_row_with_values([]))
#print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
#print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def distance(first,second):
    '''Returns the edit distance between the first and second string'''
    if not first:
        return len(second)
    if not second:
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:],second[1:])
    
    substitution = 1 + distance(first[1:],second[1:])
    deletion = 1 + distance(first[1:],second)
    insertion = 1 + distance(first,second[1:])
    
    return min(substitution, deletion, insertion)
#print(distance("humbuger","hamburger"))
    
