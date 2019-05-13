'''
Created on Feb 24, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
import unittest
import hw4

class Test(unittest.TestCase):
    def test01(self):
    # Replace pass with real test code. Use self.assertEqual. pass
    # Write more tests...
        self.assertEqual(hw4.pascal_row(6), [1,6,15,20,15,6,1])
    
    def test02(self): 
        self.assertEqual(hw4.pascal_row(7), [1,7,21,35,35,21,7,1])
    
    def test03(self):
        self.assertEqual(hw4.pascal_row(8), [1,8,28,56,70,56,28,8,1])
    
    def test04(self):
        self.assertEqual(hw4.pascal_row(20), [1,20,190,1140,4845,15504,38760,77520,125970,167960,184756,167960,125970,77520,38760,15504,4845,1140,190,20,1])
    
    def test05(self):
        self.assertEqual(hw4.pascal_row(16),[1,16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1820,560,120,16,1])
        
    def test06(self):
        self.assertEqual(hw4.pascal_triangle(6),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1] ])
    
    def test07(self):
        self.assertEqual(hw4.pascal_triangle(7),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1] ])
    
    def test08(self):
        self.assertEqual(hw4.pascal_triangle(8),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1] ])
    
    def test09(self):
        self.assertEqual(hw4.pascal_triangle(9),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1] ])
    
    def test10(self):
        self.assertEqual(hw4.pascal_triangle(10),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1],[1,10,45,120,210,252,210,120,45,10,1] ])
if __name__ == "__main__":
        unittest.main()

