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


rows_input = get_user_input("Enter the number of rows for the array: ")
cols_input = get_user_input("Enter the number of columns for the array: ")

try:
    rows = int(rows_input)
    cols = int(cols_input)
except ValueError:
    print("Error: Invalid input for rows or columns. Please enter valid integers.")
    exit()

user_input_values = []

for i in range(rows):
    row_input = get_user_input(f"Enter space-separated values for row {i + 1} (of length {cols}): ")

    try:
        row_values = [int(num) for num in row_input.split()]
    except ValueError:
        print("Error: Invalid input for array values. Please enter valid integers.")
        exit()

    if len(row_values) != cols:
        print(
            f"Error: The provided number of values in row {i + 1} does not match the specified number of columns ({cols}).")
        exit()

    user_input_values.extend(row_values)

arr = np.array(user_input_values).reshape((rows, cols))

print("Iterating over the 2-D array:")
for row in arr:
    print(row)
