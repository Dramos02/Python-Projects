import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

import numpy as np

user_input = input("Enter space-separated (ex.1 2 3) numbers to create a NumPy array: ")

# validate
while not user_input.strip():
    print("Field cannot be empty. Please try again.")
    user_input = input("Enter space-separated (ex.1 2 3) numbers to create a NumPy array: ")

user_numbers = [int(num) for num in user_input.split()]

# Create a NumPy array from the list
arr = np.array(user_numbers)

print("Element at index 0:", arr[0])

#validate
while True:
    index_1 = input("Enter the index for the first element: ")
    index_2 = input("Enter the index for the second element: ")

    if index_1.strip() and index_2.strip():
        index_1 = int(index_1)
        index_2 = int(index_2)
        break
    else:
        print("Error: Indices cannot be empty. Please try again.")

# Print the sum of elements at specified indices
sum_of_elements = arr[index_1] + arr[index_2]
print(f"Sum of elements at index {index_1} and {index_2}: {sum_of_elements}")