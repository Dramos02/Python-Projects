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


# Custom ufunc for logarithm base 12
def dominiclog(x):
    return np.log(x) / np.log(12)


# Wrap the function with np.frompyfunc
ufunc_dominiclog = np.frompyfunc(dominiclog, 1, 1)

number_input = get_user_input("Enter a positive number: ")

try:
    number = float(number_input)
    if number <= 0:
        print("Error: Input must be a positive number.")
        exit()
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
    exit()

# Calculate logarithmic operations
log2_result = np.log2(number)
log_e_result = np.log(number)
log10_result = np.log10(number)

# Calculate custom logarithm at base 12 using the ufunc
log12_result = ufunc_dominiclog(number)

# Print the results
print(f"The logarithm base 2 of {number} is: {log2_result}")
print(f"The natural logarithm (base e) of {number} is: {log_e_result}")
print(f"The logarithm base 10 of {number} is: {log10_result}")
print(f"The logarithm base 12 (dominiclog) of {number} is: {log12_result}")
