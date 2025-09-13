import time
from concurrent.futures import ThreadPoolExecutor

# 1. Normal Function
def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

# 2. Generator Function
def print_number_generator(numbers):
    for number in numbers:
        time.sleep(1)
        yield f"Number: {number}"

# 3. Multithreading version
def print_number_multithreading(numbers):
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)
        return results
    
# ---------------------------------------------------
if __name__ == '__main__':
    numbers = list(range(1,6))

    # Normal function
    print("\nRunning Normal Function:")
    start_time1 = time.time()
    for number in numbers:
        print(print_number(number))
    end_time1 = time.time()

    # Generator function
    print("\nRunning Generator Function:")
    start_time2 = time.time()
    for result in print_number_generator(numbers):
        print(result)
    end_time2 = time.time()

    # Multithreading function
    print("\nRunning Multithreading Function:")
    start_time3 = time.time()
    for result in print_number_multithreading(numbers):
        print(result)
    end_time3 = time.time()

    # Final Summary
    print("\n Time Taken Summary: ")
    print(f"Normal Function: {end_time1 - start_time1:.2f} seconds")
    print(f"Generator Function: {end_time2 - start_time2:.2f} seconds")
    print(f"Multithreading: {end_time3 - start_time3:.2f} seconds")