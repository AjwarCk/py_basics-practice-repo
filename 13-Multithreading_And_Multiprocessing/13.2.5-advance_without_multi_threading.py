## Without multithreading

import time

# 1. Normal function
def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

# 2. Generator function
def print_number_generator(numbers):
    for number in numbers:
        time.sleep(1)
        yield f"Number: {number}"

# -----------------------------------
if __name__ == '__main__':
    numbers = list(range(1,6))

    # Normal Function call
    start_time1 = time.time()
    print("\nRunning Normal Function:")
    for number in numbers:
        print(print_number(number))
    end_time1 = time.time()

    # Generator function
    start_time2 = time.time()
    print("\nRunning Generator Function:")
    for result in print_number_generator(numbers):
        print(result)
    end_time2 = time.time()

    # Final Summary
    print("\nTime Taken Summary:")
    print(f"Normal Function: {end_time1 - start_time1:.2f} seconds")
    print(f"Generator Function: {end_time2 - start_time2:.2f} seconds")
