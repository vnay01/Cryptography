###### Imports
import math
import time
from datetime import datetime

script_start_time = datetime.now()

def prime_factor(n):

    x = math.sqrt(n)        # Square root of number
    print(int(x))

    if (n > 1):
        for x in range(2, int(x)+1):
            if (n % x == 0):
                return 0
                break
        else:
            return 1    # Condition for prime
    else:
        return 0


## Factorization function

if __name__ == '__main__':
#    n = 235616869893895625763911
    n = 235616869



if (prime_factor(n) == 1 ):
            print("Prime")
else:
    print("Not Prime")

## timing information
script_end_time = datetime.now()
print(script_end_time - script_start_time)
