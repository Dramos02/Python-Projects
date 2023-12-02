import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please try again.")


def get_boolean_values():
    while True:
        bool_input = get_user_input("Enter space-separated True/False values for filtering: ").lower()

        if all(val in ['true', 'false'] for val in bool_input.split()):
            return [val == 'true' for val in bool_input.split()]
        else:
            print("Error: Invalid input for boolean values. Please enter True or False.")


values_input = get_user_input("Enter space-separated values for the array: ")

try:
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Error: Invalid input for array values. Please enter valid integers.")
    exit()

arr = np.array(values)

bool_values = get_boolean_values()

newarr = arr[bool_values]

# Print the filtered array
print("\nFiltered Array:")
print(newarr)