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


number_input = get_user_input("Enter a number: ")

try:
    number = float(number_input)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
    exit()

trunc_result = np.trunc(number)
fix_result = np.fix(number)
around_result = np.around(number)
floor_result = np.floor(number)
ceil_result = np.ceil(number)

# Print the results
print(f"The truncated value of {number} is: {trunc_result}")
print(f"The rounded value of {number} using fix() is: {fix_result}")
print(f"The rounded value of {number} using around() is: {around_result}")
print(f"The floor value of {number} is: {floor_result}")
print(f"The ceiling value of {number} is: {ceil_result}")
