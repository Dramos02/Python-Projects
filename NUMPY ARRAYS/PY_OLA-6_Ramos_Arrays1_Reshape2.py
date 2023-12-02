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


values_input = get_user_input("Enter space-separated values for the array: ")

try:
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Invalid input for array values. Please enter valid integers.")
    exit()

arr = np.array(values)

dim1 = int(get_user_input("Enter the size of the first dimension: "))
dim2 = int(get_user_input("Enter the size of the second dimension: "))
dim3 = int(get_user_input("Enter the size of the third dimension: "))

newarr = arr.reshape(dim1, dim2, dim3)

print("reshape your 1D Array to 3D Array")
print("\nOriginal Array:")
print(arr)

print("\nReshaped Array:")
print(newarr)