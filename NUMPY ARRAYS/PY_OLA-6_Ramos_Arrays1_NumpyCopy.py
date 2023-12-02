import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


# validation
def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Field cannot be empty. Please try again.")


array_input = get_user_input("Enter space-separated string values for the array: ")

while not array_input.strip():
    print("\nField cannot be empty. Please try again.")
    array_input = get_user_input("Enter space-separated (ex.1 2 3) numbers to create a NumPy array: ")

# string - integer
user_input_values = [int(num) for num in array_input.split()]

arr = np.array(user_input_values)
numpy_copy = arr.copy()

print("Orignal Numpy Array:", arr)
print("Copy of Numpy Array:", numpy_copy)