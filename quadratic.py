'''
Created on Apr 24, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
from math import sqrt
class QuadraticEquation():
    def __init__(self,a,b,c):
        try:
            3/a
        except:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        return self.__b * self.__b - 4*self.__a*self.__c
    
    def root1(self):
        discriminant_val = self.discriminant()
        if discriminant_val < float(0):
            return None
           
        return (-1*self.__b + sqrt(discriminant_val))/(2 * self.__a)
    
    def root2(self):
        discriminant_val = self.discriminant()
        if discriminant_val < float(0):
            return None
           
        return (-1*self.__b - sqrt(discriminant_val))/(2 * self.__a)
    
    def __str__(self):
        sign_a = ''
        sign_b = ''
        sign_c = ''
        a = self.__a
        b = self.__b
        c = self.__c
        if a < 0:
            sign_a = '-'
            if a== -1.0:
                a = ''
        elif a > 0:
            sign_a = ''
            if a == 1.0:
                a = ''
        if b< 0:
            sign_b = '-'
            if b== -1.0:
                b = ''
            else:
                b = str(self.__b)[1:]
        elif b > 0:
            sign_b = '+'
            if b == 1.0:
                b = ''
        if c< 0:
            sign_c = '-'
            c = str(self.__c)[1:]
        elif c> 0:
            sign_c = '+'
        elif c == 0:
            c = ''
        
        if self.__a != 0 and self.__b != 0 and self.__c!= 0:
            return f'{sign_a}{a}x^2 {sign_b} {b}x {sign_c} {c} = 0'
        elif self.__a != 0 and self.__b == 0 and self.__c!= 0:
            return f'{sign_a}{a}x^2 {sign_c} {c} = 0'
        elif self.__a == 0 and self.__b != 0 and self.__c!= 0:
            return f'{sign_b} {b}x {sign_c} {c} = 0'
        elif self.__a == 0 and self.__c == 0:
            return f'{sign_b} {b}x = 0'
        elif self.__b == 0 and self.__c == 0:
            return f'{sign_a}{a}x^2 = 0'
        if self.__a != 0 and self.__b != 0 and self.__c== 0:
            return f'{sign_a}{a}x^2 {sign_b} {b}x = 0'
'''
    too much work:
    if self.__b == 0 and self.__c == 0:
            return f'{self.__a}x^2 = 0'
        elif self.__a == 1 and self.__b == 0 and self.__c == 0 :
            return 'x^2 = 0'
        elif  self.__a == 1 and self.__b == 0:
            return f'x^2 + {self.__c} = 0'
        elif  self.__a == 1 and self.__c == 0:
            return f'x^2 + {self.__b}x = 0'
        elif self.__a == 1 and self.__b == 1 and self.__c == 0:
            return 'x^2 + x = 0'
        elif self.__a == 1 and self.__b == 1 :
            return f'x^2 + x + {self.__c} = 0'
        elif self.__c == 0:
            return f'{self.__a}x^2 + {self.__b}x = 0'
        elif self.__b == 0:
            return f'{self.__a}x^2 + {self.__c} = 0'
        elif self.__a == 1:
            return f'x^2 + {self.__b}x + {self.__c} = 0'
        
        
        
        elif self.__a == -1 and self.__b == 0 and self.__c == 0 :
            return '-x^2 = 0'
        elif  self.__a == -1 and self.__b == 0:
            return f'-x^2 + {self.__c} = 0'
        elif  self.__a == -1 and self.__c == 0:
            return f'-x^2 + {self.__b}x = 0'
        elif self.__a == -1 and self.__b == -1 and self.__c == 0:
            return '-x^2 - x = 0'
        elif self.__a == -1 and self.__b == -1 :
            return f'-x^2 - x + {self.__c} = 0'
        elif self.__a == -1:
            return f'-x^2 + {self.__b}x + {self.__c} = 0'
            
        inefficient and doesn't work:
        something = [f'{self.__a}x^2',f'{self.__b}x']
        something = list(map(lambda x: '' if float(x[:x.index('x')]) == 0 else x[x.index('x'):] if float(x[:x.index('x')]) == 1.0 \
            else '-' + x[x.index('x'):] if x[0] == '-'else x,something))
        if self.__c !=0 and len(something[1]) > 0:
            x = something[1]
            if x[0] != '-' and self.__c < 0 :
                return something[0] + ' + ' + something[1] + ' - ' + str(self.__c)[1:] + ' = 0'
            elif x[0] != '-'and self.__c > 0 :
                return something[0] + ' + ' + something[1] + ' + ' + str(self.__c) + ' = 0'
            
            elif x[0] == '-' and self.__c < 0 :
                return something[0] + ' - ' + something[1][1:] + ' - ' + str(self.__c)[1:] + ' = 0'
            elif x[0] == '-'and self.__c > 0 :
                return something[0] + ' - ' + something[1][1:] + ' + ' + str(self.__c) + ' = 0'
            
        elif :
            return something[0] + something[1] + ' = 0'
'''