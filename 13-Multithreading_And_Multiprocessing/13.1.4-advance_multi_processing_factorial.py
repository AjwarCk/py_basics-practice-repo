## Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time
import math
import sys

sys.set_int_max_str_digits(100000)

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == '__main__':

    numbers = [5000,6000,7000,8000]

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=11) as executor:
        results = executor.map(computer_factorial,numbers)

    for result in results:
        print(result)

    end_time = time.time()

    print(f"Total time in seconds: {end_time - start_time}")