import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

start_time = time.time()

# Function calls
square_numbers()
cube_numbers()

end_time = time.time()

print(f"Finished time: {end_time - start_time}")