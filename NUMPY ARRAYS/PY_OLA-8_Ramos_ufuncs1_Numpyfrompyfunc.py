import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def dominicadd(x, y):
    return x + y


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


x = get_vector_input("x")

y = get_vector_input("y")

ufuncadd = np.frompyfunc(dominicadd, 2, 1)

result = ufuncadd(x, y)

# Print the result
print("\nResult of Vector with own function(dominicadd) Addition:")
print(result)