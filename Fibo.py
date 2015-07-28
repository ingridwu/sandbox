import sys
import os
import traceback
def fab(number):
    if number == 0 or number == 1:
        return 1
    else:
        return (fab(number -1) + fab(number-2))

try:
    init_value = int(sys.argv[1])
    if init_value < 0:
        raise ValueError
    fab_number = fab(init_value)
    print "The Fab # is %d" % fab_number
except ValueError:
    print "Please input integer"
except:
    print "Unknown error"
finally:
    print "The input number is [%s]" % sys.argv[1]
