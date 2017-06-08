# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 20:20:54 2017

@author: wade
"""

class Calculator:

    def mod(self, dividend, divisor):
        remainder = dividend % divisor
        quotient = (dividend - remainder) / divisor
        return quotient, remainder

if __name__ == '__main__':
    cal = Calculator()
    assert cal.mod(5, 3) == (1, 2) # 5 / 3 = 1 ... 2
    assert cal.mod(8, 4) == (1, 0) # 8 / 4 = 2 ... 0