 '''
CS 115, Sky OOP Activity

Author: Bharddwaj Vemulapalli    
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement the missing sections of the Star class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import math
from random import randint

class Star(object):

    def __init__(self, x, y):
        '''Initializes the PRIVATE fields x and y with the values received as
        arguments. You may assume x and y are valid integers.'''
        self.__x = x
        self.__y = y

    # Write properties for x and y.
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        self.__y = y

    # Write the method that checks if this Star is equal to another Star here.
    # Two Stars are equal if their x and y coordinates are equal. Be sure
    # to overload the correct operator for use with ==.
    def __eq__(self,other):
        return self.__x == other.x and self.__y == other.y

    def distance_to(self, other):
        '''Computes the distance to the other Star passed as an argument to
        the method.
        Recall the distance formula (not written in valid Python syntax):
        d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        '''
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)

    def __str__(self):
        '''Returns the string representation of the location of the Star, such
        as (3, 2) or (-1, 5). Note the space after the comma.'''
        return '(' + str(self.__x) +', ' + str(self.__y) + ')'

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement the missing sections of the Sky class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Sky(object):

    def __init__(self):
        '''Initializes the Sky object with between 5-10 Stars randomly
        generated.'''
        self.__stars = []
        for _ in range(randint(5, 10)):
            self.__stars.append(Star(randint(-100, 100), randint(-100, 100)))

    def westernmost_star(self):
        '''Returns the western most Star in the Sky (Star with the lowest x
        value).'''
        minimum = self.__stars[0]
        
        for i in range(1,len(self.__stars)):
            if self.__stars[i].x < minimum.x:
                minimum = self.__stars[i]
                
        
        return minimum
                

    def northernmost_star(self):
        '''Returns the northern most Star in the Sky (Star with the highest y
        value).'''
        maximum = self.__stars[0]
        
        for i in range(1,len(self.__stars)):
            if self.__stars[i].y > maximum.y:
                maximum = self.__stars[i]
                
        
        return maximum

    def __str__(self):
        '''Returns a string representation of the list of coordinates of the
        Stars in the Sky.'''
        return '[' + ', '.join(map(str, self.__stars)) + ']'

if __name__ == '__main__':
    star1 = Star(3, 6)
    star2 = Star(4, -3)
    print('Star 1: %s' % star1)
    print('Star 2: %s' % star2)
    print('Star 1\'s x-coordinate: %d' % star1.x)
    print('Star 2\'s y-coordinate: %d' % star2.y)
    print('Stars equal? %s' % (star1 == star2))
    print('Distance? %.2f' % star1.distance_to(star2))

    sky = Sky()
    print('\nStars in sky at:')
    print(sky)
    print('Westernmost star at: %s' % sky.westernmost_star())
    print('Northernmost star at: %s' % sky.northernmost_star())
