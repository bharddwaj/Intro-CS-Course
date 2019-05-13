'''
Created on Feb 6, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''

'''Helper Functions'''
def length(lst):
    '''Returns the length of the list'''
    if not lst:
        return 0
    else:
        return 1 + length(lst[:-1])
    
def even(X):
    if X % 2 == 0 : 
        return True
    else: 
        return False
''' ''' ''' ''' ''' ''' ''' ''' ''' '''    
def dot(L, K):
    '''outputs the dot product of the lists L and K'''
    if not L or not K:
        return 0
    
       # return "Error the two lists are not the same size"
    return L[0] * K[0] + dot(L[1:],K[1:])
#print(dot([5,3], [6,4]))

def explode(S):
    '''take a string S as input and should return a list of the characters (each of
which is a string of length 1) in that string'''
    if not S:
        return []
    return [S[0]] + explode(S[1:])
#print(explode('spam'))
#print(explode(''))

def ind(e, L):
    '''takes in an element e and a sequence L then returns the index at which e is first found in L.'''
    if not L:
        return 0 #what assert wants me to return
    elif e == L[0]:
        return 0
    return 1 + ind(e,L[1:])

print(ind(42, [ 55, 77, 42, 12, 42, 100 ]))
print(ind(42, range(0,100)))
print(ind('hi', [ 'hello', 42, True ]))
print(ind('hi', [ 'well', 'hi', 'there' ]))
print(ind('i', 'team'))
print(ind(' ', 'outer exploration'))

def removeAll(e, L):
    '''takes in an element e and a list L. Then, removeAll should return another list that is identical to L
     except that all elements identical to e have been removed.'''
    funcall = ind(e,L)
    if funcall != length(L):
        #this means that e is within the list
        L = L[:funcall] + L[1+funcall:]
        return removeAll(e,L) 
    else:
        return L
#print(removeAll(42, [ 55, 77, 42, 11, 42, 88 ]))
#print(removeAll([77, 42], [ 55, [77, 42], [11, 42], 88 ]))

def myFilter(predicate,lst):
    '''returns a new list that contains all of the elements of L for which the predicate returns True'''
    if not lst:
        return []
    elif predicate(lst[0]):
        return [lst[0]] + myFilter(predicate, lst[1:])
    return myFilter(predicate, lst[1:])

#print(my_filter(even, [0, 1, 2, 3, 4, 5, 6]))

def deepReverse(L):
    '''takes as input a list of elements where some of those elements may be lists themselves.
    deepReverse returns the reversal of the list where,
    additionally, any element that is a list is also deepReversed.'''
    if not L:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]
    
#print(deepReverse([1, 2, 3]))
#print(deepReverse([1, [2, 3], 4]))
#print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))

