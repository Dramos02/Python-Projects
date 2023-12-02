import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


# validation
def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Field cannot be empty. Please try again.")


def create_numpy_array():
    # Get user input for the array values with validation
    array_input = get_user_input("Enter space-separated values for the array: ")

    # Convert the user input string into a list of integers
    user_input_values = [int(num) for num in array_input.split()]

    # Get user input for the data type with validation
    dtype_input = get_user_input("Enter the desired data type for the array (e.g., 'S' or 'i4'): ")

    # Create a NumPy array from user input values and specified data type
    arr = np.array(user_input_values, dtype=dtype_input)

    # Print the array and its data type
    print(f"Array: {arr}")
    print(f"Data type of the array: {arr.dtype}")


# Loop to allow the user to create arrays multiple times
while True:
    create_numpy_array()

    # Ask the user if they want to create another array
    repeat = get_user_input("Do you want to create another array? (yes/no): ").lower()
    if repeat != 'yes':
        break