import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

user_input = input("\nEnter space-separated (ex.1 2 3) numbers to create a NumPy array: ")

# validation
while not user_input.strip():
    print("\nField cannot be empty. Please try again.")
    user_input = input("Enter space-separated (ex.1 2 3) numbers to create a NumPy array: ")

user_numbers = [int(num) for num in user_input.split()]

arr = np.array(user_numbers)

print("NumPy array:", arr)
print("Type of the array:", type(arr))
