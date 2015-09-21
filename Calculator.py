from sys import exit

from Collector import Collector

class Calculator:

    '''
    In charge of calculating collatz numbers.
    '''
    
    def __init__(self, collector):
        self.collector = collector
    
    def calculate(self, num):
        '''
        calculate the next number in the collatz sequence for num
        '''
        if num == 2:
            return 1
        if num < 2:
            print('uh oh! {} is not following the rules!'.format(num))
            exit(1)
            return None
        collatz_number = self.collector.get_collatz_number(num)
        if collatz_number is None:
            if num % 2 == 0:
                collatz_number = num / 2
            else:
                collatz_number = (3 * num) + 1
            self.calculate(collatz_number)
            self.collector.set_collatz_number(num, collatz_number)
        #print('{}:{}'.format(num, collatz_number))
        
        return self.collector.get_collatz_chain(num)
            
if __name__ == '__main__':
    collector = Collector()
    calculator = Calculator(collector)
    for n in range(2, 1000000):
        #print('{}: {}'.format(n, calculator.calculate(n)))
        chain = calculator.calculate(n)
