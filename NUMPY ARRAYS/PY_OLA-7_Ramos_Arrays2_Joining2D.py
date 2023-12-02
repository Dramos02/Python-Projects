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


def create_2d_array(rows, cols, array_number):
    print(f"Enter values for Array {array_number} ({rows} rows, {cols} columns):")
    array_values = []

    for i in range(rows):
        row_input = get_user_input(f"Enter space-separated values for row {i + 1}: ")

        try:
            row_values = [int(num) for num in row_input.split()]
        except ValueError:
            print("Error: Invalid input for array values. Please enter valid integers.")
            exit()

        if len(row_values) != cols:
            print(f"Error: Number of values in row {i + 1} does not match the specified number of columns ({cols}).")
            exit()

        array_values.append(row_values)

    return np.array(array_values)


rows1_input = get_user_input("Enter the number of rows for Numpy Array 1: ")
cols1_input = get_user_input("Enter the number of columns for Numpy Array 1: ")

rows2_input = get_user_input("Enter the number of rows for Array 2: ")
cols2_input = get_user_input("Enter the number of columns for Array 2: ")

try:
    rows1, cols1, rows2, cols2 = map(int, [rows1_input, cols1_input, rows2_input, cols2_input])
except ValueError:
    print("Error: Invalid input for rows or columns. Please enter valid integers.")
    exit()

# Create the two 2-D arrays based on user input
arr1 = create_2d_array(rows1, cols1, 1)
arr2 = create_2d_array(rows2, cols2, 2)

if arr1 is not None and arr2 is not None:
    # Concatenate the two arrays along rows (axis=1)
    arr = np.concatenate((arr1, arr2), axis=1)
    print("\nConcatenated Array along rows (axis=1):")
    print(arr)