import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

# Start time
start_time = time.time()

# Calling functions
square_numbers()
cube_numbers()

# end time
end_time = time.time()

print(f'Total time it took: {end_time - start_time}')