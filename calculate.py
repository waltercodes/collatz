# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:00:53 2015

@author: Walter Scott
"""

import argparse

from Collector import Collector
from Calculator import Calculator

if __name__ == '__main__':
    collector = Collector()
    calculator = Calculator(collector)

    parser = argparse.ArgumentParser()
    parser.add_argument("first", help="first number in sequence", type=int)
    parser.add_argument("last", help="last number in sequence", type=int)
    args = parser.parse_args()   
    
    for n in range(args.first, args.last):
        #print('{}: {}'.format(n, calculator.calculate(n)))
        chain = calculator.calculate(n)
        
