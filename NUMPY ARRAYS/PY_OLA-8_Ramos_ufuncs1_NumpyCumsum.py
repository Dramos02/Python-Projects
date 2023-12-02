import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            try:
                return np.array([int(num) for num in user_input.split()])
            except ValueError:
                print("Error: Invalid input. Please enter valid integers.")
        else:
            print("Error: Input cannot be empty. Please try again.")


user_array = get_user_input("Enter space-separated values for the array: ")

cumulative_sum = np.cumsum(user_array)

print("\nCumulative Sum:")
print(cumulative_sum)
