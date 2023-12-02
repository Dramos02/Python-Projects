import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

# validation
while True:
    user_input = input("Enter space-separated (ex.1 2 3) numbers for a NumPy array (ndmin=5): ")

    if user_input.strip():
        try:
            arr = np.array([int(num) for num in user_input.split()], ndmin=5)

            print("NumPy array:", arr)
            print("Number of dimensions:", arr.ndim)
            break

        except ValueError:
            print("Error: Please enter valid numbers.")
    else:
        print("Error: Input cannot be empty. Please try again.")
