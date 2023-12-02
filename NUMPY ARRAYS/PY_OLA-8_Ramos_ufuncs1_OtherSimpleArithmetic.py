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

divisor_input = get_user_input("Enter a divisor: ")

try:
    divisor = int(divisor_input)
    if divisor == 0:
        print("Error: Divisor cannot be zero.")
        exit()
except ValueError:
    print("Error: Invalid input for divisor. Please enter a valid integer.")
    exit()

mod_result = np.mod(number, divisor)
remainder_result = np.remainder(number, divisor)
divmod_result = np.divmod(number,divisor)
absolute_value_abs = np.absolute(divmod_result)
abs_value = np.abs(divmod_result)


# Print the results
print(f"The modulo of {number} divided by {divisor} is: {mod_result}")
print(f"The remainder of {number} divided by {divisor} is: {remainder_result}")
print(f"The divmod of {number} divided by {divisor} is: {divmod_result}")
print(f"The absolute value of {number} using absolute() is: {absolute_value_abs}")
print(f"The absolute value of {number} using abs() is: {abs_value}")