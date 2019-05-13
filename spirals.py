'''
Created on Feb 25, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''

import turtle

def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        if walls == count:
            turtle.done()
            
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(distance + initial * (count % 2), initial, count + 1)
            

    square_spiral_helper(20, 20, 0)

def octagonal_spiral(walls):
    def octagonal_spiral_helper(distance, initial, count):
        if walls == count:
            turtle.done()
            
        else:
            turtle.left(45)
            turtle.forward(distance)
            octagonal_spiral_helper(distance + initial * (count % 2), initial, count + 1)
            

    octagonal_spiral_helper(20, 5, 0)