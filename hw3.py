'''
Created on February 14, 2019
@author:   Bharddwaj Vemulapalli
username:  bvemulap
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
#from bigdict import Dictionary
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount,coins):
    '''takes the same kind of input
as change but returns a list whose first item is the minimum number of coins and whose second item is a list of the coins in that optimal solution. '''
    if amount == 0:
        return [0,[]]
    if amount < 0:
        return [float("inf"),[]]
    if not coins:
        return [float("inf"),[]]
    #return min(1 + change(amount - coins[0],coins), change(amount,coins[1:]) )
    use_it_call = giveChange(amount - coins[0],coins)
    lose_it_call = giveChange(amount,coins[1:])
    use_it = [ 1 + use_it_call[0],use_it_call[1] + [coins[0]] ]
    
    if use_it[0] < lose_it_call[0]:
        return use_it
    return lose_it_call
#print(giveChange(48, [1, 5, 10, 25, 50]))   
#print(giveChange(48, [1, 7, 24, 42]))
#print(giveChange(35, [1, 3, 16, 30, 50]))
 
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Helper Functions
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter,scorelist):
    '''input a single letter string called letter and a list where each element in that list is itself a list of the form [character,
value] where character is a single letter and value is a number associated with that letter (e.g. it's scrabble score). The letterScore function 
then returns a single number, namely the value associated with the given letter.'''
    if not scorelist:
        return 0
    elif isinstance(scorelist[0], list):
        return letterScore(letter, scorelist[0]) or letterScore(letter, scorelist[1:])
    elif scorelist[0] == letter:
        return scorelist[1]
    return letterScore(letter, scorelist[1:])

def wordScoreALT(scorelist):
    '''input a string S and a scorelist in the format described above, which will have only lowercase letters,
     and should return as output the scrabble score of that string'''
    def secondaryHelper(S):
        if not S:
            return 0
        else:
            return letterScore(S[0],scorelist) + secondaryHelper(S[1:])
    return secondaryHelper
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if not dct:
        return ['',0]
    # mapping the wordScoreALT to each word in the dictionary and i was able to use this map
    # by modifying the wordScore function so it only takes in one argument that stays constant (scores)
    # and iterates through the dictionary
    return  list(map(lambda x:[x] + [wordScoreALT(scores)(x)],dct))
#print(wordsWithScore(Dictionary, scrabbleScores))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if len(L) == 1: 
        #have to go until index n -1
        return []
    return [L[0]] + take(n,L[1:])
#print(take(3, [0,1,2,3]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n >= len(L):
        return []
    return [L[n]] + drop(n + 1, L)
#print(drop(8, [0,1,2,3,4,5,6,7,8,9]))


