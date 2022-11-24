## Prime factor calculator
## Finds all the prime numbers till a given number
## Additionally stores the primes numbers in a file.
import math
import time
from time import process_time
from pathlib import Path
import os

from datetime import datetime

class prime_cal():

    def prime_cal(num):
        n = num
        primes = []

    # Check is the number is greater than 1
        # Outer loop to step through the range of numbers i.e  2 to 'X'
        for i in range(2, n+1):
            # Actual loop to check whether the current outer loop number is prime or not
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    break
            else:
                primes.append(i)

        return primes

# Start Logging time
script_start_time = process_time()

# main function
# Number provided : 235616869893895625763911
N = 30
if __name__ == '__main__':

    a = prime_cal(N)

    print(a)

script_end_time = process_time()
total_time_elapsed = (((script_end_time - script_start_time)))
print(total_time_elapsed,'s')

## Storing generated numbers in a file
# Create a file paths
file_path = "E:\Cryptography"
file_name = 'PrimeNumbers.txt'


# Write generated prime numbers into the new file
with open(file_name, 'w') as file_object:
    file_object.write('List of prime number upto: ')
    file_object.write(str(N))
    file_object.write('\n')
    file_object.write('\n')

    for i in range(len(a)):
        file_object.write(str(a[i]))
        file_object.write('\n')
    file_object.write('Total Time elapsed: ')
    file_object.write(str(total_time_elapsed))
    file_object.write(' s')
    file_object.write('\n')
    file_object.write('Number of prime numbers ')
    file_object.write(str(len(a)))


#closing file
file_object.close()
