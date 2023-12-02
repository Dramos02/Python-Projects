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


def sort_array():
    values_input = get_user_input("Enter space-separated values for the array: ")

    try:
        values = values_input.split()
    except ValueError:
        print("Error: Invalid input for array values. Please enter valid values.")
        exit()

    arr = np.array(values)

    # Determine the data type of the array (int or str) to apply sorting accordingly
    dtype = int if all(val.isdigit() or val.lstrip('-').isdigit() for val in values) else str

    # Sort the array
    sorted_arr = np.sort(arr)

    print("\nSorted Array:")
    print(sorted_arr)


while True:
    sort_array()

    user_input = get_user_input("Do you want to input another array? (yes/no): ").lower()

    while user_input not in ['yes', 'no']:
        print("Error: Please enter 'yes' or 'no'.")
        user_input = get_user_input("Do you want to input another array? (yes/no): ").lower()

    if user_input == 'no':
        break
