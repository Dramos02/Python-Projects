import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def get_vector_input(vector_name):
    while True:
        user_input = input(f"Enter space-separated values for vector {vector_name}: ")
        if user_input.strip():
            try:
                # Convert the user input string into a NumPy array of integers
                return np.array([int(num) for num in user_input.split()])
            except ValueError:
                print(f"Error: Invalid input for vector {vector_name}. Please enter valid integers.")
        else:
            print(f"Error: Input for vector {vector_name} cannot be empty. Please try again.")

# Get user input for vector x
x = get_vector_input("x")

# Get user input for vector y
y = get_vector_input("y")

# Perform vector addition using NumPy's add function
z = np.add(x, y)

# Print the result
print("\nResult of Vector Addition:")
print(z)