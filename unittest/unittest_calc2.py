# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 21:33:22 2017

@author: wade
"""

import unittest

class Cal:
    def mod(self, dividend, divisor):
        remainder = dividend % divisor
        quotient = (dividend - remainder) / divisor
        return quotient, remainder
    
class CalTest(unittest.TestCase):
    def setUp(self):
        self.cal = Cal()
        
    def tearDown(self):
        self.cal = None
    
    def test_mod_with_remainder(self):
        self.assertEqual(self.cal.mod(5,3),(1,2))
        
    def test_mod_without_remander(self):
        self.assertEqual(self.cal.mod(8,4),(1,0))
    
    def test_mod_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.cal.mod, 7, 1) 

if __name__ == "__main__":
        unittest.main()