### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers = list(range(1,16))

if __name__ == '__main__':

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)

    end_time = time.time()

    print(f"Result: {list(results)}")
    print(f"Total time: {end_time - start_time} seconds.")