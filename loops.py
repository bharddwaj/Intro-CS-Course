'''
Created on Apr 1, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
import random
import time
def find_max(lst):
    if lst == []:
        return None
    else:
        max = lst[0]
        for x in lst:
            if x > max:
                max = x
        return max

def find_min_max(lst):
    '''Return a tuple of (min,max)'''
    if lst == []:
        return None
   
    else:
        min = max = lst[0]
        for x in lst:
            if x <  min:
                min = x
            elif x > max:
                max = x
        return min,max #don't need parentheses when you return a tuple

def shallow_copy(lst):
    new_list = []
    for x in lst:
        new_list.append(x) 
    return new_list

def shallow_copy_list_comp(lst):
    return [x for x in lst]

L = [1,2,3]
M = shallow_copy_list_comp(L)
#L[0] = 11
#print(L)
#print(M)

#print(id(L[1]), id(M[1]))

def deep_copy(lst):
    new_list = []
    for x in lst:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

board = [
    [3,0,1],
    [2,5,6],
    [-9,8,7],
    [1,2,3]
    ]

def addall(board):
    total = 0
    for lst in board:
        for element in lst:
            total += element
    return total

def addall2(board):
    total = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            total += board[row][col]
    return total

#print(addall2(board))
#print(addall(board))

def sequential_search(lst,key):
    '''Returns the index of the key if it's present or -1 if it's not'''
    ''' O(n) '''
    for i in range(0,len(lst)):
        if lst[i] == key:
            return i
    return -1

#print(sequential_search([3,7,-1,2,12,8], 2))
#print(sequential_search([3,7,-1,2,12,8], 13))

def binary_search(lst,key):
    ''' O(log_2_(n)) '''
    low = 0
    high = len(lst) -1 
    while low <= high:
        #mid = (low + high)//2
        mid = low + (high-low)//2
        if key == lst[mid]:
            return mid
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -low - 1 #take the negative(low) - 1 to find where the key should be inserted.
                    #-1 is there so there is no ambiguity when the index is 0
    
#random_list = [random.randint(1,1000000) for _ in range(10000000)]
#start = time.time()
#print(sequential_search(random_list, 2000000))
#print(f"Elapsed Time: {(time.time() - start)*1000} ms")
#random_list.sort()
#start = time.time()
#random_list.sort()
#print(binary_search(random_list, 2000000))
#print(f"Elapsed Time for Binary Search: {(time.time() - start)*1000} ms")

def swap(a,b,lst):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1): #highest index i can be is n - 2
        min_index = i
        for j in range(i+1,n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(i,min_index,lst)

lst = [random.randint(1,100000) for _ in range(20000)]
start_time = time.time()
#selection_sort(lst)
#print(lst)
lst.sort()
print(f"Elapsed Time for Selection Sort: {(time.time() - start_time)*1000} ms")