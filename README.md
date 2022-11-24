# Cryptography

## Description

I am taking a course in Cryptography at school. This repo contains code which can be used to implement the math used in various Cryptographic algorithms

### Dependencies
All the code is developed and executed on PYCHARM. Please install the packages:

#datetime : can used to see the execution time of your code

#memory-profiler: used to check the memory usage of various functions


### Current Status:
This repo is in development phase. I am stuck with a 'MemoryError' while calling
prim_factor():* 

```
"""
for i in range(len(rSqrModN)):
    a = prim.prim_factor(rSqrModN[i])
    if max(a) < B:
        rValue_B_smooth.append(rSqrModN[i])
"""
```


*Once I figure the issue causing this, I can proceed further...probably during the first week of December
