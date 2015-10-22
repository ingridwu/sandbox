import sys
import os
import traceback
class Fib:
    def __init__(self):
        self.fib_list = [1, 1]
        return
    def fib2(self, number):
        '''
            fib_list[0] = 1 count = 1
            fib_list[1] = 1 count = 2
            fib_list[2] = 2 count = 3
            fib_list[n-1] = fib[n-2] + fib[n-3]
            n = 1, 2, ...., 3
        '''
        if number < 2:
            return self.fib_list[number -1]
        count = len(self.fib_list)
        while(count <= number):
            new_value = self.fib_list[count-1] + self.fib_list[count -2]
            self.fib_list.append(new_value)
            count +=1
            
        return self.fib_list[count -1]

    def fib(self, number):
        if number == 1 or number == 2:
            return 1
        else:
            return (self.fib(number -1) + self.fib(number-2))

myFib = Fib()
try:
    init_value = int(sys.argv[1])
    if init_value <= 0:
        raise ValueError 
    fab_number = myFib.fib2(init_value)
    print "The Fab # is %d" % fab_number
except ValueError:
    print "Please input integer"
except IndexError:
    print "Usage : python Fibo.py [integer]"
except:
    print "Unknown error", sys.exc_info()[0]
else:
    print "The input number is [%s]" % sys.argv[1]
