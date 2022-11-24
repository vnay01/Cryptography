###### Imports
import sys
import math
import time

from memory_profiler import memory_usage
from datetime import datetime

# User defined function import
from functions import prime_cal



num = 10
##### Choosing Smoothness bound
##### Remember that the choice of Smoothness bound dictates the amount of memory
##### required for the factor-base
B = 30

#### Create object for prime_cal
prim = prime_cal()

#### List below contains factor base
F = prim.prime_num(2,B)

####### Creating L values
L = len(F) + 5

####### Calculating r value
rValue = []
for k in range(3):
    for j in range(3):
        r= math.floor(math.sqrt(k * num)) + j
        rValue.append(r)
type(rValue)
##### Calculating (r^2 mod num) and stored in the form of a list rSqr
rSqrModN = []
for i in range(len(rValue)):
    rSqr = int((rValue[i]*rValue[i])%num)
    rSqrModN.append(rSqr)

"""
##### Copying list generated from 
test_num = []
for item in rSqrModN:
    test_num.append(item)
"""

##### Discard (rSqr mod num) values which are not B-smooth
rValue_B_smooth = []
"""
for i in range(len(rSqrModN)):
    a = prim.prim_factor(rSqrModN[i])
    if max(a) < B:
        rValue_B_smooth.append(rSqrModN[i])
"""

"""
for i in range(len(rSqrModN) - 1):
    a = prim.prim_factor(rSqrModN[i])
    rValue_B_smooth.append(a)
"""



mem_usage = memory_usage(prim.prim_factor(rSqrModN[4]))

###### ###### ###### ###### REMOVE BLOCK BEFORE GIT PUSH ###### ###### ###### ######
##### Test prints

print('Printing rValue',rValue, 'of type', type(rValue))

print('Printing rSqrModN',rSqrModN, 'of type ', type(rSqrModN), 'and size ', sys.getsizeof(rSqrModN))

#print('Printing factors of a ',a)

print('Printing rValue_B_smooth', rValue_B_smooth,  'and size ', sys.getsizeof(rValue_B_smooth))
print('Printing size without overhead', rSqrModN.__sizeof__())

print('Maximum memory usage : ' ,max(mem_usage))