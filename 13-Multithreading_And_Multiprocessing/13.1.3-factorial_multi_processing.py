'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial Calculations, especially for large numbers,
Involve significant computational work. Multiprocessing can be used to
distibute the workload accross multiple CPU cores, improving performance.
'''

import time
import sys
import math
import multiprocessing

# max int value
sys.set_int_max_str_digits(100000)

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == '__main__':

    numbers = [5000,6000,7000,8000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time took in seconds: {end_time - start_time}")