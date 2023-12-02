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


values_input = get_user_input("Enter space-separated values for the array (e.g., 1 2 3): ")

try:
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Error: Invalid input for array values. Please enter valid integers.")
    exit()

arr = np.array(values)

# Reshape the array to a 3-D array (based on code snippet)
arr = arr.reshape((2, 2, 2))

# Iterate over the 3-D array using nditer
print("Iterating over the 3-D array using nditer:")
print(arr)
for x in np.nditer(arr):
    print(x)
