import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


array_input = input("Enter space-separated string values for the array: ")

#validation
while not array_input.strip():
    print("\nField cannot be empty. Please try again.")
    array_input = input("Enter space-separated string to create a NumPy array: ")

# instead of int, I made str for string
user_input_values = [str(num) for num in array_input.split()]

#np.values
arr = np.array(user_input_values)

# Print the data type of the array
print(f"Data type of the array: {arr.dtype}")
