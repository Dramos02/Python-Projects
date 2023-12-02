import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

# array dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize a list
user_input_values = []

# values
for i in range(rows):
    row_input = input(f"Enter space-separated (ex.1 2 3) values for row {i + 1}: ")
    # validation
    while not row_input.strip():
        print("Error: Row values cannot be empty. Please try again.")
        row_input = input(f"Enter space-separated (ex.1 2 3) values for row {i + 1}: ")
    # string - integer
    row_values = [int(num) for num in row_input.split()]
    user_input_values.append(row_values)

# np.array
arr = np.array(user_input_values)
print(arr)

# validation
while True:
    row_index = int(input("Enter the row index: "))
    col_index = int(input("Enter the column index: "))

    # validate not out of bounds
    if 0 <= row_index < arr.shape[0] and 0 <= col_index < arr.shape[1]:
        break
    else:
        print("Error: Invalid indices.")

# Print the element at the specified indices
print(f"Element at row {row_index}, column {col_index}: {arr[row_index, col_index]}")
