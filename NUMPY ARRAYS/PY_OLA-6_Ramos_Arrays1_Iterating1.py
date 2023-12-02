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


values_input = get_user_input("Enter space-separated (ex. 1 2 3 ) values for the array: ")

try:
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Error: Invalid input for array values. Please enter valid integers.")
    exit()

arr = np.array(values)

print("Iterating over the 1-D array:")
for x in arr:
    print(x)
