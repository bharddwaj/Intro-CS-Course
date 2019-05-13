'''
Created on February 7, 2019
@author:   Bharddwaj Vemulapalli
username: bvemulap
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
#import time
#from cs115 import map, reduce, filter
#from dict import Dictionary
#from bigdict import Dictionary
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo','spam', 'spammy', 'zzyzva']

# Implement your functions here.
''' Helper Functions '''
def length(lst):
    '''Returns the length of the list'''
    if not lst:
        return 0
    else:
        return 1 + length(lst[:-1])
    
def member(x,lst):
    '''returns true if x is contained in the list and false otherwise'''
    ''' Tail Recursion '''
    if not lst:
        return False
    
    elif x == lst[0]:
        return True
    
    else:
        return member(x, lst[1:])

''' ''' ''' ''' ''' ''' ''' '''

def letterScore(letter, scorelist):
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
#print(letterScore("x", scrabbleScores))
#print(letterScore("a", scrabbleScores))

def wordScore(S, scorelist):
    '''input a string S and a scorelist in the format described above, which will have only lowercase letters,
     and should return as output the scrabble score of that string'''
    if not S:
        return 0
    else:
        return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)
#print(wordScore('spam', scrabbleScores))
#print(wordScore("wow", [['o', 10], ['w', 42]]))

def scoreList(Rack):
    '''input a Rack which is a list of lower-case letters and returns a list of all of the words
     in the global Dictionary that can be made from those letters and the score for each one. '''
    def checkEach(dictionary_index,rack):
        '''Returns a string of letters that are present within that word'''
       
        if not dictionary_index or not rack:
            return ''
        
        elif member(dictionary_index[0],rack):
            some_index = rack.index(dictionary_index[0]) #after testing I realized that each letter in the rack can only be used once
            return dictionary_index[0] + checkEach( dictionary_index[1:],rack[0:some_index] + rack[some_index+1:])
        
        return ''
    def apply_on_every_word(dictionary):
        if not dictionary:
            return []
        return [checkEach(dictionary[0], Rack)] + apply_on_every_word(dictionary[1:])
    def is_length_equal(lst,dictionary):
        '''If the length is equal then returns the word along with its score in  list of lists'''
        if not lst or not dictionary:
            return []
        elif length(lst[0]) == length(dictionary[0]):
            return [[lst[0],wordScore(lst[0],scrabbleScores)]] + is_length_equal(lst[1:], dictionary[1:])
        else:
            return is_length_equal(lst[1:], dictionary[1:])
        
    #alt_list = apply_on_every_word(Dictionary)
    #is_length_equal(apply_on_every_word(Dictionary), Dictionary)
    return is_length_equal(apply_on_every_word(Dictionary), Dictionary)
#startTime = time.time()  
#print(scoreList(["a", "s", "m", "t", "p"])) 
#print(scoreList(["a", "s", "m", "o", "f", "o"]))
#print(scoreList(['w', 'y', 'l', 'e', 'l', 'o']))
#print(scoreList(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z']))
#print(f"it took {-1*(startTime - time.time())}")
def scoreList2(Rack):
    '''input a Rack which is a list of lower-case letters and returns a list of all of the words
     in the global Dictionary that can be made from those letters and the score for each one. '''
    
    def checkEach(dictionary_index,rack):
        '''Returns a string of letters that are present within that word'''
        
        if not dictionary_index or not rack:
            return ''
        
        elif dictionary_index[0] in rack:
            some_index = rack.index(dictionary_index[0]) #after testing I realized that each letter in the rack can only be used once
            return dictionary_index[0] + checkEach( dictionary_index[1:],rack[0:some_index] + rack[some_index+1:])
        
        return ''
    def checkEach2(dictionary_index,rack):
        #I have no idea why this is partially working; doesn't rlly work with 'a' but the rest of dictionary is fine?
        return list(map(lambda x,y: y[0:y.index(x)] + y[y.index(x) + 1:] if x in y and not y.startswith(x)  else x if y.startswith(x) else  '',dictionary_index,rack))
   
    def apply_on_every_word(dictionary):
        if not dictionary:
            return []
        return [checkEach(dictionary[0], Rack)] + apply_on_every_word(dictionary[1:])
    
    def apply_on_every_word2(dictionary):
        if not dictionary:
            return []
        return [checkEach2(dictionary[0], Rack)] + apply_on_every_word(dictionary[1:]) 
       
    primary_list = apply_on_every_word(Dictionary)
    #alt_list =  apply_on_every_word2(Dictionary)
    
    #if the rack can make the word which is checked by map comparing the lengths, then wordScore function is called,
    #filter removes all the leftover empty lists
    return list(filter(lambda x: x != [],map(lambda x,y: [x,wordScore(x,scrabbleScores)] if len(x) == len(y) else [],primary_list,Dictionary)))
    #return is_length_equal(some_list, Dictionary)
#startTime = time.time()    
#print(scoreList2(["a", "s", "m", "t", "p"])) 
#print(scoreList2(["a", "s", "m", "o", "f", "o"]))
#print(scoreList2(['w', 'y', 'l', 'e', 'l', 'o'])) 
#Ans:[['leo', 3], ['low', 6], ['lowly', 11], ['ow', 5], ['owe', 6], ['owl', 6], ['we', 5], ['well', 7], ['woe', 6], ['yell', 7], ['yo', 5]]
#print(scoreList2(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z']))
#print(f"it took {-1*(startTime - time.time())}")
def bestWord(Rack):
    '''takes as input a Rack as above and returns a list with two elements: the highest possible scoring word
     from that Rack followed by its score. If there are ties, they can be broken arbitrarily.'''
    a_list_of_possible_words = scoreList(Rack)
    def highest_score(lst,some_index):
        '''Checks which word has the highest score and returns that word with its score'''
        if not lst:
            return some_index
        elif lst[0][1] > some_index[1]:
            some_index = lst[0]
            return highest_score(lst[1:], some_index)
        else:
            return highest_score(lst[1:], some_index)
            
    if a_list_of_possible_words:  
        return highest_score(a_list_of_possible_words,a_list_of_possible_words[0])
    return ['', 0] #if no possible words can be created then return 0 and an empty string
#print(bestWord(["a", "s", "m", "t", "p"]))
#print(bestWord(['w', 'y', 'l', 'e', 'l', 'o']))
#print(bestWord(["s", "p", "a", "m", "y"]))
#print(bestWord(["s", "p", "a", "m", "y", "z"]))