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


dim1_input = get_user_input("Enter the size of the first dimension: ")
dim2_input = get_user_input("Enter the size of the second dimension: ")
dim3_input = get_user_input("Enter the size of the third dimension: ")

try:
    dim1 = int(dim1_input)
    dim2 = int(dim2_input)
    dim3 = int(dim3_input)
except ValueError:
    print("Error: Invalid input for dimensions. Please enter valid integers.")
    exit()

user_input_values = []

for i in range(dim1):
    for j in range(dim2):
        row_input = get_user_input(
            f"Enter space-separated values for row {j + 1} in dimension {i + 1} (of length {dim3}): ")

        try:
            row_values = [int(num) for num in row_input.split()]
        except ValueError:
            print("Error: Invalid input for array values. Please enter valid integers.")
            exit()

        # Check if the length of the row matches the specified number of elements in the third dimension
        if len(row_values) != dim3:
            print(
                f"Error: The provided number of values in row {j + 1} does not match the specified number of elements "
                f"in dimension {i + 1} ({dim3}).")
            exit()

        user_input_values.extend(row_values)

arr = np.array(user_input_values).reshape((dim1, dim2, dim3))

print("Iterating over the 3-D array:")
print(arr)
for x in arr:
    for y in x:
        for z in y:
            print(z)
