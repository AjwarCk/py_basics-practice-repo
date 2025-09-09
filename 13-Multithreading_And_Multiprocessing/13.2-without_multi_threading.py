import time

def print_numbers(n):
    for i in range(n):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters(str):
    for i in str:
        time.sleep(2)
        print(f"Letter: {i}")


if __name__ == '__main__':

    # start time
    start_time = time.time()

    # function calls
    print_numbers(5)
    print_letters('abcde')

    # end time
    end_time = time.time()

    print(f"Total time {end_time - start_time} seconds took.")

