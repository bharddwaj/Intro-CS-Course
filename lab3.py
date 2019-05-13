'''
Created on Feb 14, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
 
def change(amount, coins):
    '''Returns a non-negative integer indicating the minimum number of coins required to make up the givenamount.'''
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")
    if coins == []:
        return float("inf")
    return min(1 + change(amount - coins[0],coins), change(amount,coins[1:]) )
'''
doesn't work haha
def change2(amount,coins):
    
    if amount == 0:
        return 0
    if amount <= 0:
        return float("inf")
    if coins == []:
        return float("inf")
    max_coin_value = max(coins)
    max_index = coins.index(max_coin_value)
    
    list_of_modulars = list(map(lambda x: amount % x ,coins))
    min_remainder = min(list_of_modulars)
    filtered_list_coins = list(filter(lambda x: amount % x == min_remainder,coins))
    min_remainder_index = coins.index(max(filtered_list_coins)) #trying to find biggest number with smallest remainder
    
    # added this portion to remove 1 until later to see if it fixes algorithm
    index_for_one = coins.index(1)
    coins2 = coins[:index_for_one] + coins[index_for_one + 1:]
    
    list_of_modulars2 = list(map(lambda x: amount % x ,coins2))
    
    min_remainder2 = min(list_of_modulars2)
    
    filtered_list_coins2 = list(filter(lambda x: amount % x == min_remainder2,coins2))
    
    min_remainder_index2 = coins2.index(max(filtered_list_coins2))
    ###########################################################################
    #print(max(filtered_list_coins))
    #print(amount)
     
    
    #subtracting_max_first = 1 + change2(amount - coins[max_index], coins)
    mod_with_one = 1 + change2(amount - coins[min_remainder_index] , coins)
    print(f"this is modulus with 1: {coins[min_remainder_index]}")
    mod_without_one = 1 + change2(amount - coins2[min_remainder_index2],coins)
    print(f"this is modulus without 1: {coins2[min_remainder_index2]}")
    
    return min(mod_with_one,mod_without_one)
'''
#print(change(48, [1, 5, 10, 25, 50]) ) #supposed to be 6
#print(change(48, [1, 7, 24, 42]) )     #supposed to be 2
#print(change(35, [1, 3, 16, 30, 50]) ) #supposed to be 3