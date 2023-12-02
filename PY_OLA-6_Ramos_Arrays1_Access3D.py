import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

depth = int(input("Enter the number of depth dimensions: "))
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

user_input_values = []

for d in range(depth):
    user_input_rows = []
    for i in range(rows):
        row_input = input(f"Enter space-separated (ex.1 2 3) values for depth {d + 1}, row {i + 1}: ")
        # validation
        while not row_input.strip():
            print("Error: Row values cannot be empty. Please try again.")
            row_input = input(f"Enter space-separated (ex.1 2 3) values for depth {d + 1}, row {i + 1}: ")
        # string - integer
        row_values = [int(num) for num in row_input.split()]
        user_input_rows.append(row_values)
    user_input_values.append(user_input_rows)

# np.array
arr = np.array(user_input_values)

# validation
while True:
    depth_index_input = input("Enter the depth index: ")
    row_index_input = input("Enter the row index: ")
    col_index_input = input("Enter the column index: ")

    # validate not out of bounds
    if depth_index_input.strip().isdigit() and row_index_input.strip().isdigit() and col_index_input.strip().isdigit():
        depth_index = int(depth_index_input)
        row_index = int(row_index_input)
        col_index = int(col_index_input)

        if 0 <= depth_index < arr.shape[0] and 0 <= row_index < arr.shape[1] and 0 <= col_index < arr.shape[2]:
            break
        else:
            print("Try Again, Out of Bounds.")
    else:
        print("Try Again: Invalid indices.")

# Print the element at the specified indices
print(f"Element at depth {depth_index}, row {row_index}, column {col_index}: {arr[depth_index, row_index, col_index]}")
