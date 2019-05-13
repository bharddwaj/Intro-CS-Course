'''
Created on Feb 20, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
def knapsack(capacity, itemList):
    '''returns both the maximum value and the list of items that make this value, without exceeding the capacity of your knapsack.'''
    if not itemList:
        return [0, []]
    if capacity == 0:
        return [0,[]]
    
    loseIt = knapsack(capacity, itemList[1:])
    if capacity - itemList[0][0] >= 0:
        useIt = knapsack(capacity - itemList[0][0], itemList[1:])
        result = [itemList[0][1] + useIt[0],[itemList[0]] + useIt[1]]
        if result[0] > loseIt[0]:
            return result
    
    
    
    return loseIt
#print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
    
