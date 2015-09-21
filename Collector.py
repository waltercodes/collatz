# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:46:19 2015

@author: Walter Scott
"""

class Collector:
    '''
    Collects collatz numbers and allows the calculator to look for existing numbers
    '''
    
    def __init__(self):
        self.collatz_numbers = {2: 1}
    
    def get_collatz_number(self, number):
        '''
        do a lookup to see if the collatz number for num already exists
        '''
        if number in self.collatz_numbers:
            return self.collatz_numbers[number]
        return None
            
    def set_collatz_number(self, number, collatz_number):
        '''
        allows calculator to save the results of a collatz calculation so we only
        have to calculate it once
        '''
        self.collatz_numbers[number] = collatz_number
        
    def get_collatz_chain(self, number):
        '''
        return a string with the chain from the number to 1
        '''
        i = number
        chain = str(number)
        while self.collatz_numbers[i] > 1:
            chain = chain + ' -> ' + str(self.collatz_numbers[i])
            i = self.collatz_numbers[i]
        return chain + ' -> 1'

if __name__ == '__main__':
    collector = Collector()
    print('Returns None when the number does not exist: {}'.format(collector.get_collatz_number(5)))
    collector.set_collatz_number(5, 16)
    print('After setting the number for 5 to 16: {}'.format(collector.get_collatz_number(5)))
    