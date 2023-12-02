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


values_input = get_user_input("Enter space-separated (ex. 1 2 3 ) values for the array: ")

try:
    # string - integer
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Invalid input for array values. Please enter valid integers.")
    exit()

# np array
arr = np.array(values)

# user input of dimension

new_shape_input = get_user_input("Enter space-separated (ex. 4 3 ) shape for the array: ")

try:
    # Convert the user input string into a list of integers
    new_shape = [int(num) for num in new_shape_input.split()]
except ValueError:
    print("Invalid input for array shape. Please enter valid integers.")
    exit()

# Reshape the array based on user input
newarr = arr.reshape(*new_shape)

# Print the original and reshaped arrays
print("reshape your 1D Array to 2D Array")
print("\nOriginal Array:")
print(arr)

print("\nReshaped Array:")
print(newarr)
