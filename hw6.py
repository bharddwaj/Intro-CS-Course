'''
Created on March 6th, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#the professor is lying because if there is frequent changes between 0 and 1, it is inevitable that the algorithm
#returns more bits than the original string

####Helper Functions######
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    #true if odd
    return n % 2 != 0

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n == 1:
        return '1'
    if isOdd(n):
        return numToBinary(n//2) + f'{n % 2}' 
    else:
        return numToBinary(n//2) + '0' 

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s == '1':
        return 1
    elif s[0] == '1':
        return 2 ** (len(s)-1) + binaryToNum(s[1:])
    else:
        #if s[0] == '0'
        return binaryToNum(s[1:])
def length_normalizer(s):
    '''Adds 0s in front of the binary number to make the length equal to the compressed block size'''
    
    if COMPRESSED_BLOCK_SIZE > len(s): 
        #not bigger than max number of numbers in a row but the binary number is not 
        #the proper length
        s = (COMPRESSED_BLOCK_SIZE - len(s))*'0'+ s
    
    return s
###############################################

#largest number of bits compress could use is 64*COMPRESSED_BLOCK_SIZE + COMPRESSED_BLOCK_SIZE.
#assuming 64 bit string, if it alternates between 0 and 1 then u use COMPRESSED_BLOCK_SIZE 64 times. 
#now if it starts with 1 you have to include COMPRESSED_BLOCK_SIZE*'0' in front so thats why i added C_B_S to get the max

def compress(s):
    '''takes a binary string S of length 64 as input
     and returns another binary string as output. '''
    
    def compress_helper(s):
        # the .index() method returns the first index that the element appears in the list
        if len(s) > 0:
            
            if s[0] == '0' and '1' in s or s[0] == '1' and '0' in s:
                if s[0] == '0':
                    the_index = s.index('1')
                else:
                    the_index = s.index('0')
                number_in_a_row = the_index #shows number in a row until that index
                
                #print(f'0 and 1: {number_in_a_row}')
                
                if number_in_a_row > MAX_RUN_LENGTH:
                    #if the number of the characters in a row is bigger than max number of characters that could be in a row defined by  binaryToNum(COMPRESSED_BLOCK_SIZE*'1')
                    #then will simply split it into max numbers + '0' for zero 1s and then + the rest of the numbers in a row
                    #this could theoretically be recursive so that there is no threshold based on number of if statements i have
                    #luckily the condition is that it's a 64 bit string so these 2 if statements should be enough
                    #if i didn't procrastinate i could've used recursion or another better method haha.
                    
                    if number_in_a_row - MAX_RUN_LENGTH > MAX_RUN_LENGTH:
                        return '1'*COMPRESSED_BLOCK_SIZE + '0'*COMPRESSED_BLOCK_SIZE + '1'*COMPRESSED_BLOCK_SIZE + '0'*COMPRESSED_BLOCK_SIZE + length_normalizer(numToBinary(number_in_a_row - 2*MAX_RUN_LENGTH)) + compress_helper(s[the_index:])
                    else:
                        return '1'*COMPRESSED_BLOCK_SIZE + '0'*COMPRESSED_BLOCK_SIZE + length_normalizer(numToBinary(number_in_a_row - MAX_RUN_LENGTH)) + compress_helper(s[the_index:])
                else: 
                    number_in_a_row = length_normalizer(numToBinary(number_in_a_row))
                    return  number_in_a_row + compress_helper(s[the_index:])
                
            elif s[0] == '0' or s[0] == '1':
                number_in_a_row = len(s)
                
                #print(f'1 or 0: {number_in_a_row}')
                
                if number_in_a_row > MAX_RUN_LENGTH:
                    
                    if number_in_a_row - MAX_RUN_LENGTH > MAX_RUN_LENGTH:
                        return '1'*COMPRESSED_BLOCK_SIZE + '0'*COMPRESSED_BLOCK_SIZE + '1'*COMPRESSED_BLOCK_SIZE + '0'*COMPRESSED_BLOCK_SIZE + length_normalizer(numToBinary(number_in_a_row - 2*MAX_RUN_LENGTH))
                    else:
                        return '1'*COMPRESSED_BLOCK_SIZE + '0'*COMPRESSED_BLOCK_SIZE + length_normalizer(numToBinary(number_in_a_row - MAX_RUN_LENGTH))
                else: 
                    number_in_a_row = length_normalizer(numToBinary(number_in_a_row))
                    return  number_in_a_row
        
        else:
            return '0'*2*COMPRESSED_BLOCK_SIZE
        
    if s[0] == '1':
        return '0'*COMPRESSED_BLOCK_SIZE + compress_helper(s)
    else:
        return compress_helper(s)
        
       
    
def uncompress(C):
    '''grab first MRL which would be zeroes, convert it to decimal multiply by '0', 
    then grab the next block which would be 1s and convert it to decimal and multiply by '1', 
    go back and forth'''
    ''' given a compressed C, this function returns the original string s'''
    if not C:
        return ''
    elif len(C) <= COMPRESSED_BLOCK_SIZE:
        return binaryToNum(C[0:len(C)])*'0' 
    elif len(C) < 2*COMPRESSED_BLOCK_SIZE:
        return binaryToNum(C[0:COMPRESSED_BLOCK_SIZE])*'0' + binaryToNum(C[COMPRESSED_BLOCK_SIZE:len(C)])*'1'
    else:
        return binaryToNum(C[0:COMPRESSED_BLOCK_SIZE])*'0' + binaryToNum(C[COMPRESSED_BLOCK_SIZE:2*COMPRESSED_BLOCK_SIZE])*'1' + uncompress(C[2*COMPRESSED_BLOCK_SIZE:])

       

def compression(S):
    '''return the ratio of the compressed size to the original size for image S.'''
    return len(compress(S))/len(S)

Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
Five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"

#print(compress(Penguin)) #00011000100010100100001000010000100001000001100110000010100000010001000010000001000100000100010
#print(uncompress(compress(Penguin)) == Penguin) #True
#print(compression(Penguin)) #1.484375
assert(compress('0000000000000000000000000000000000000000000000000000000000000000') == '1111100000111110000000010')
assert(compress('0101010101010101010101010101010101010101010101010101010101010101') == '00001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
assert(uncompress('111110000000001111110000000001') == '0000000000000000000000000000000011111111111111111111111111111111')
assert(compression('0000000000000000000000000000000011111111111111111111111111111111') == 0.46875)

print('hi')
#print(compress(Smile)) #0100100010000100001000010000100001000010011010000100100000010010000001000100011001001
#print(uncompress(compress(Smile)) == Smile) #True
#print(compression(Smile)) #1.328125

#print(compress(Five)) #00000010010011100001001110000100111001110100000001001110100000001
#print(uncompress(compress(Five)) == Five) #True
#print(compression(Five)) #1.015625

