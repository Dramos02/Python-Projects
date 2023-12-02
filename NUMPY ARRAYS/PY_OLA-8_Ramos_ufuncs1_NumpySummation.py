import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def get_array_input(array_name):
    while True:
        user_input = input(f"Enter space-separated values for array {array_name}: ")
        if user_input.strip():
            try:
                # Convert the user input string into a NumPy array of integers
                return np.array([int(num) for num in user_input.split()])
            except ValueError:
                print(f"Error: Invalid input for array {array_name}. Please enter valid integers.")
        else:
            print(f"Error: Input for array {array_name} cannot be empty. Please try again.")


arr1 = get_array_input("arr1")

arr2 = get_array_input("arr2")

result_axis_1 = np.sum([arr1, arr2], axis=1)
summation_result = np.add(arr1, arr2)

print("\nResult of Summation along axis 1:")
print(summation_result)
print(result_axis_1)
