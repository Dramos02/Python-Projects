import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please try again.")

values_input = get_user_input("Enter space-separated values for the array: ")

try:
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Error: Invalid input for array values. Please enter valid integers.")
    exit()

arr = np.array(values)

parts_input = get_user_input("Enter the number of parts to split the array into: ")

try:
    num_parts = int(parts_input)
except ValueError:
    print("Error: Invalid input for the number of parts. Please enter a valid integer.")
    exit()

# Split the array into the specified number of parts
newarr = np.array_split(arr, num_parts)

print(f"\nOriginal Array: {arr}")
print(f"\nArray after splitting into {num_parts} parts:")
for i, sub_array in enumerate(newarr, start=1):
    print(f"Part {i}: {sub_array}")
