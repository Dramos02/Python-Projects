print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def get_vector_input(vector_name):
    while True:
        user_input = input(f"Enter space-separated values for vector {vector_name}: ")
        if user_input.strip():
            try:
                return [int(num) for num in user_input.split()]
            except ValueError:
                print(f"Error: Invalid input for vector {vector_name}. Please enter valid integers.")
        else:
            print(f"Error: Input for vector {vector_name} cannot be empty. Please try again.")


x = get_vector_input("x")

y = get_vector_input("y")

z = [i + j for i, j in zip(x, y)]

print("\nResult of Vector Addition:")
print(z)