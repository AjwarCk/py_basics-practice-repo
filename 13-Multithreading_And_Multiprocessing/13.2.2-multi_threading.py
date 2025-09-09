## Multithreading
## When to use Multi Threading
## I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
## Concurrent execution: When you want to improve the throughout of your application by performing multiple operations concurrently.

import time
import threading

def print_numbers(n):
    for i in range(n):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters(s):
    for i in s:
        time.sleep(2)
        print(f"Letter: {i}")

if __name__ == '__main__':

    t1 = threading.Thread(target=print_numbers, args=(5,))
    t2 = threading.Thread(target=print_letters, args=('abcde',))

    start_time = time.time()

    ## start the thread
    t1.start()
    t2.start()

    ## Wait for the threads to complete
    t1.join()
    t2.join()

    end_time = time.time()

    print(f"Total {end_time - start_time} seconds took.")