# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:00:53 2015

@author: Walter Scott
"""

import argparse

from Collector import Collector
from Calculator import Calculator
from threading import Timer

def print_status():
    print(n)
    timer = Timer(60, print_status)
    timer.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("first", help="first number in sequence", type=int)
    parser.add_argument("last", help="last number in sequence", type=int)
    parser.add_argument("--hidechains", help="don't print the full path from each number to 1", dest='print_chains', action='store_false')
    parser.add_argument("--showchains", help="print the full path from each number to 1", dest='print_chains', action='store_true')
    args = parser.parse_args()   
    
    collector = Collector()
    calculator = Calculator(collector, args.print_chains)
    
    n = 0
    
    if not args.print_chains:
        print_status()
    
    for n in range(args.first, args.last):
        #print('{}: {}'.format(n, calculator.calculate(n)))
        chain = calculator.calculate(n)
        if args.print_chains:
            print('{}'.format(chain))
    
    # if we made it this far, the range must be valid
    print('it looks like the conjecture holds for the range from {} to {}.'.format(args.first, args.last))
    timer.cancel()