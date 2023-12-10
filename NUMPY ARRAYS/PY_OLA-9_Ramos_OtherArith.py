import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


# I created my own numpyfrompyfunc for power, remainder, qoutient&remainder and absolute
def dominicpower(x, y):
    return x ** y


def dominicremainder(x, y):
    return np.remainder(x, y)


def dominicquotient_remainder(x, y):
    quotient, remainder = np.divmod(x, y)
    return quotient, remainder


def dominicabsolute(x):
    return np.absolute(x)


def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please try again.")



while True:
    print("\nSimple Arithmetic Operations")
    print("[1] Power")
    print("[2] Remainder")
    print("[3] Quotient and Remainder")
    print("[4] Absolute")

    choice = get_user_input("Please enter your choice (1-4): ")

    # Created a dictionary for arithmetic operations
    operations = {
        '1': 'Power',
        '2': 'Remainder',
        '3': 'Quotient and Remainder',
        '4': 'Absolute'
    }
    if choice not in operations:
        print("Invalid choice. Please choose a number from 1 to 4.")
        continue

    # then it will show the operations based on user's choice
    print(f"\nPerforming {operations[choice]} operation:\n")

    # Get size of the array based on user's input
    size = int(get_user_input("Enter size of the array: "))

    # Get elements for the array based on the user's input
    while True:
        arr1 = np.array(
            [int(num) for num in get_user_input(f"Enter elements for array 1 (ex. 1 2 3) (of size {size}): ").split()])
    # The loop will continue till the right amount of elements is based on the size
        if len(arr1) == size:
            break
        else:
            print(f"Error: Number of elements should be {size}. Please try again.")

    while True:
        arr2 = np.array(
            [int(num) for num in get_user_input(f"Enter elements for array 2 (ex. 1 2 3) (of size {size}): ").split()])
        if len(arr2) == size:
            break
        else:
            print(f"Error: Number of elements should be {size}. Please try again.")

    print(f"\nArray 1: {arr1}")
    print(f"Array 2: {arr2}\n")

    # Perform my own function with numpy based on user's choice
    if choice == '1':
        result = np.frompyfunc(dominicpower, 2, 1)(arr1, arr2)
        print(f"\nPower value is {result}.")
    elif choice == '2':
        result = np.frompyfunc(dominicremainder, 2, 1)(arr1, arr2)
        print(f"\nRemainder value is {result}.")
    elif choice == '3':
        quotient, remainder = np.frompyfunc(dominicquotient_remainder, 2, 2)(arr1, arr2)
        print(f"\nQuotient: {quotient}, Remainder: {remainder}.")
    elif choice == '4':
        result = np.frompyfunc(dominicabsolute, 1, 1)(arr1)
        result_arr2 = np.frompyfunc(dominicabsolute, 1, 1)(arr2)
        print(f"\nAbsolute values for Array One:{result} and \n{result_arr2}.")

    # The user will have the choice to perform another basic arithmetic operation
    while True:
        another_operation = get_user_input("\nDo you want to perform another operation? (yes/no): ").lower()
        if another_operation in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    if another_operation != 'yes':
        break
