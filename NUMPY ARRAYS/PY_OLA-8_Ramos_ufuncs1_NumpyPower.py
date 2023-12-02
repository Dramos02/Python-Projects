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

result = np.power(number, 2)

print(f"The square of {number} is: {result}")