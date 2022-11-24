import math
import time
from datetime import datetime
from pathlib import Path
import os
from memory_profiler import memory_usage



class prime_cal():

    def __init__(self):
        return
#        prime_cal(num)

    def prime_num(self, a, n):
        """Not an efficient implementation"""
        # Returns a list of all prime numbers less than or equal to 'N'
        primes = []

        # Check is the number is greater than 1
        # Outer loop to step through the range of numbers i.e  2 to 'X'
        for i in range(a, n + 1):
            # Actual loop to check whether the current outer loop number is prime or not
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)

        return primes


    def factor(self, n):
        """Returns all factors of given number"""
        # Absoultely NOT efficient
        factor = []

        for i in range(2, (n)):
            if n % i == 0:
                factor.append(i)

        ## Returns a list of factors
        return factor


    def prim_factor(self, n):
        """takes a number and gives back the list with only prime factors"""
        prim_factors = []
        num = n

        while num % 2 == 0:
            prim_factors.append(2)
            num = num / 2

        for i in range(3, int(math.sqrt(num) + 1),2):
            while num % i == 0:
                prim_factors.append(i)
                num = num / i
        # If 'num' is prime then it needs to be added too!
        if num > 2:
            prim_factors.append(int(num))

        return prim_factors




#################### test Code - DELETE before Final deployment ####################################
"""
N = 8937651
c = prime_cal()
#print(c.prime_num(1,100))
script_start_time = int(round(time.time()))
#print(c.factor(N))
#print(len(c.factor(N)))
print(c.prim_factor((N)))
script_end_time = int(round(time.time() ))
total_time_elapsed = (((script_end_time - script_start_time)))
print(total_time_elapsed,'s')

c = prime_cal()
d = c.prime_num(1,100)

print(d)

"""
"""