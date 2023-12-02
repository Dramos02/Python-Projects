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

try:
    # string - integer
    rows = int(rows_input)
except ValueError:
    print("Error: Invalid input for the number of rows. Please enter a valid integer.")
    exit()

cols_input = get_user_input("Enter the number of columns for the array: ")

try:
    # string - integer
    cols = int(cols_input)
except ValueError:
    print("Error: Invalid input for the number of columns. Please enter a valid integer.")
    exit()

# store value
user_input_values = []

# array values
for i in range(rows):
    row_input = get_user_input(f"Enter space-separated values for row {i + 1} (of length {cols}): ")

    try:
        # string - integer
        row_values = [int(num) for num in row_input.split()]
    except ValueError:
        print("Invalid input for array values. Please try again.")
        exit()

    # validation for columns match rows
    if len(row_values) != cols:
        print(
            f"Error: The provided number of values in row {i + 1} does not match the specified number of columns ({cols}).")
        exit()

    # append the list
    user_input_values.append(row_values)

# np.array
arr = np.array(user_input_values)

# Print the shape of the array
print("Numpy Array:", arr)
print("Shape of the array:", arr.shape)
