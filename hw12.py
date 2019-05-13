'''
Created on Apr 27, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from functools import reduce
class Board(object):
    def __init__(self, width=7, height=6):
        '''Constructor for the class that takes in the width and height
        and initializes them to the private instance variables'''
        self.__width = width
        self.__height = height
        self.__twoD = []
        for i in range(height):
            self.__twoD.append([])
            for j in range(width):
                self.__twoD[i].append([])
                self.__twoD[i][j] = ' '
        #print(self.__twoD)
    def __str__(self):
        '''returns a string (it does not print a string) 
        representing the Board object that calls it.''' 
        
        to_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                to_str += '|' + self.__twoD[i][j]
            to_str += '\n'
        to_str +='-'*self.__width*2 
        numbers = ''
        for x in range(self.__width):
            numbers += f'{x} '
        to_str += '\n' + numbers
        return to_str #removing the first indent at the top
    
    def allowsMove(self, col):
        ''' return True if the calling Board object can allow a move into column c 
        (because there is space available). It returns False if c does not have space available
         or if it is not a valid column.'''
        if col < self.__width: #or <= self.__width - 1
            counter = 0
            for j in range(self.__height):
                if self.__twoD[j][col] == ' ':
                    counter += 1
                    break
            return counter >= 1
        return False
    
    def addMove(self, col, ox): 
        '''add an ox checker, where ox is a variable holding a string that is either "X" or "O", into column col. 
        Note that the code will have to find 
        the highest row number available in the column col and put the checker in that row. '''
        index = 0
        if self.allowsMove(col):
            for j in range(self.__height):
                if self.__twoD[j][col] == ' ':
                    if j > index:
                        index = j
            self.__twoD[index][col] = ox
            
    def delMove(self,col):
        '''remove the top checker from the column col. 
        If the column is empty, then delMove should do nothing.'''    
        index = 0
        if self.allowsMove(col):
            for j in range(self.__height):
                if self.__twoD[j][col] != ' ':
                    if j > index:
                        index = j
            self.__twoD[index][col] = ' '
    def winsFor(self, ox):
        '''Checks whether 'X' or 'O' has won the game'''  
        for i in range(self.__height):#checks if there are 4 in a row horizontal 
            for j in range(self.__width - 3): #so i don't have an indexing issue
                horizontalinarow = reduce(lambda x,y: x+y,map(lambda x:1 if x == True else 0,\
                [self.__twoD[i][j+1] == ox,self.__twoD[i][j+2] == ox,self.__twoD[i][j+3] == ox,self.__twoD[i][j] == ox]))

                if horizontalinarow == 4:
                    return True
                
        for j in range(self.__width):#checks if there are 4 in a row vertical 
            for i in range(self.__height - 3): #so i don't have an indexing issue
                verticalinarow = reduce(lambda x,y: x+y,map(lambda x:1 if x == True else 0,\
                [self.__twoD[i+1][j] == ox,self.__twoD[i+2][j] == ox,self.__twoD[i+3][j] == ox,self.__twoD[i][j] == ox]))
                
                if verticalinarow == 4:
                    return True
        
        
        for i in range(self.__height - 3):
            for j in range(self.__width - 3):
                if self.__twoD[i][j] == ox and self.__twoD[i+1][j+1] == ox \
                and self.__twoD[i+2][j+2] == ox and self.__twoD[i+3][j+3] == ox:
                    return True
        
        for i in range(self.__height - 3):
            for j in range(self.__width):
                if self.__twoD[i][j] == ox and self.__twoD[i+1][j-1] == ox \
                 and self.__twoD[i+2][j-2] ==ox and self.__twoD[i+3][j-3] == ox:
                    return True
        return False

    def hostGame( self ):
        '''run a loop allowing the user(s) to play a game. '''
        print('Welcome to Connect Four')    
        while True:
            print(self)
            x = input("X's choice: ")
            self.addMove(int(x), 'X')
            if self.winsFor('X'):
                print('X wins -- Congratulations')
                print(self)
                break
            else:
                print(self)
                o = input("O's choice: ")
                self.addMove(int(o), 'O')
                if self.winsFor('O'):
                    print('O wins -- Congratulations')
                    print(self)
                    break
            
            
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.
            
            moveString must be a string of integers
        """ 
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
   
if __name__ == '__main__':
    b = Board()
    b.hostGame()
    