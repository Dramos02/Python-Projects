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


def create_numpy_array():
    try:
        ndim = int(get_user_input("Enter the number of dimensions for the array: "))
    except ValueError:
        print("Invalid input for the number of dimensions. Please enter a valid integer.")
        return

    values_input = get_user_input("Enter space-separated values for the array: ")

    try:
        values = [int(num) for num in values_input.split()]
    except ValueError:
        print("Invalid input for array values. Please enter valid integers.")
        return

    # dimensions based on user input
    arr = np.array(values, ndmin=ndim)

    # Print the array and its shape
    print("Numpy Array:")
    print(arr)
    print("Shape of the array:", arr.shape)

    # Check if the last dimension has the value 4 based on code snippet
    if arr.shape[-1] == 4:
        print("\nLast dimension has the value 4.")
    else:
        print("\nLast dimension does not have the value 4.")


while True:
    create_numpy_array()

    loop = get_user_input("Do you want to create another array? (yes/no): ").lower()
    if loop != "yes":
        break
