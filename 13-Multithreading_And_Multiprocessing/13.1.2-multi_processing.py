## Process that run in parallel
## CPU-Bound Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution - Multiple cores of the CPU

import time
import multiprocessing

def square_numbers(n,s):
    for i in range(n):
        time.sleep(s)
        print(f"Square: {i*i}")

def cube_numbers(n,s):
    for i in range(n):
        time.sleep(s)
        print(f"Cube: {i*i*i}")

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=square_numbers, args=(5,1))
    p2 = multiprocessing.Process(target=cube_numbers, args=(5,1))

    start_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()

    print(f"Total time took: {end_time - start_time} seconds.")