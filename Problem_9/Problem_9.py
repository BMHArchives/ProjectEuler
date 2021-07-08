import numpy as np
import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def FindAnswer():
    sum = 1000
    numbers = []
    range_a = round_up(sum/3, -2),
    range_a = int(range_a[0])
    range_b = int(sum/2)
    for a in range(1,range_a):
        for b in range(1, range_b):
            c = sum - a-b
            if((a*a) + (b*b) == (c*c)):
                numbers.append(a)
                numbers.append(b)
                numbers.append(c)
                return numbers

print("Answer is: {} ".format(np.prod(FindAnswer())))
