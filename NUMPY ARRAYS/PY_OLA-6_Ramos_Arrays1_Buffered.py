import numpy as np


def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please try again.")


def create_numpy_array():
    values_input = get_user_input("Enter space-separated (ex. 1 2 3) values for the array: ")

    try:
        values = [int(num) for num in values_input.split()]
    except ValueError:
        print("Error: Invalid input for array values. Please enter valid integers.")
        exit()

    arr = np.array(values)

    dtype_input = get_user_input("Enter the data type for iteration: ")

    print("\nIterating over the array with different data types using nditer:")
    for x in np.nditer(arr, flags=['buffered'], op_dtypes=[dtype_input]):
        print(x)


while True:
    create_numpy_array()

    loop = get_user_input("Do you want to create another array? (yes/no): ").lower()
    if loop != "yes":
        break