import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty list to store user input values
user_input_values = []

# Get user input for array values
for i in range(rows):
    row_input = input(f"Enter space-separated (ex.1 2 3)values for row {i + 1}: ")
    # Validate that the input is not empty
    while not row_input.strip():
        print("Error: Row values cannot be empty. Please try again.")
        row_input = input(f"Enter space-separated (ex.1 2 3) values for row {i + 1}: ")
    # string - integer
    row_values = [int(num) for num in row_input.split()]
    user_input_values.append(row_values)

# np.array
arr = np.array(user_input_values)

# validation
while True:
    row_index_input = input("Enter the row index (accepts negative indexing): ")
    col_index_input = input("Enter the column index (accepts negative indexing): ")

    # validation
    if row_index_input.lstrip('-').isdigit() and col_index_input.lstrip('-').isdigit():
        row_index = int(row_index_input)
        col_index = int(col_index_input)

        # Adjust negative indexing
        if row_index < 0:
            row_index += rows
        if col_index < 0:
            col_index += cols

        # Print the element at the specified indices
        if -rows <= row_index < rows and -cols <= col_index < cols:
            break
        else:
            print("Try Again, Out of Bounds.")
    else:
        print("Try Again: Invalid indices.")

# Print the element at the specified indices
print(f"Element at row {row_index}, column {col_index}: {arr[row_index, col_index]}")
