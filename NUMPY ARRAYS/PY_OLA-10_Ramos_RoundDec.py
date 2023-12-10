import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


# I created my own numpyfrompyfunc for truncation, rounding, floor, ceiling, summation, cumulative summation
def dominictruncation(x):
    return np.trunc(x)


def dominicrounding(x):
    return np.round(x)


def dominicfloor(x):
    return np.floor(x)


def dominicceiling(x):
    return np.ceil(x)

def dominicsummation(x, y):
    return np.sum([x, y], axis=0)


def dominiccumulative_summation(x):
    return np.cumsum(x)

def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please try again.")



while True:
    print("\nRounding Decimals")
    print("[1] Truncation")
    print("[2] Rounding")
    print("[3] Floor")
    print("[4] Ceiling")
    print("[5] Summation")
    print("[6] Cumulative Summation")

    choice = get_user_input("Please enter your choice (1-6): ")

    # Created a dictionary for arithmetic operations
    operations = {
        '1': 'Truncation',
        '2': 'Rounding',
        '3': 'Floor',
        '4': 'Ceiling',
        '5': 'Summation',
        '6': 'Cumulative Summation'
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
            [float(num) for num in
             get_user_input(f"Enter elements for array 1 (ex. 1 2 3) (of size {size}): ").split()])
        # The loop will continue till the right amount of elements is based on the size
        if len(arr1) == size:
            break
        else:
            print(f"Error: Number of elements should be {size}. Please try again.")

    while True:
        arr2 = np.array(
            [float(num) for num in
             get_user_input(f"Enter elements for array 2 (ex. 1 2 3) (of size {size}): ").split()])
        if len(arr2) == size:
            break
        else:
            print(f"Error: Number of elements should be {size}. Please try again.")

    print(f"\nArray 1: {arr1}")
    print(f"Array 2: {arr2}\n")

    # Perform my own function with numpy based on user's choice
    if choice == '1':
        result_arr1  = np.frompyfunc(dominictruncation, 1, 1)(arr1)
        result_arr2 = np.frompyfunc(dominictruncation, 1, 1)(arr2)
        print(f"\nTruncation values for Array One {result_arr1} and \nArray Two {result_arr2}.")
    elif choice == '2':
        result_arr1  = np.frompyfunc(dominicrounding, 1, 1)(arr1)
        result_arr2 = np.frompyfunc(dominicrounding, 1, 1)(arr2)
        print(f"\nRounding values for Array One {result_arr1} and \nArray Two {result_arr2}.")
    elif choice == '3':
        result_arr1 = np.frompyfunc(dominicfloor, 1, 1)(arr1)
        result_arr2 = np.frompyfunc(dominicrounding, 1, 1)(arr2)
        print(f"\nFloor values for Array One {result_arr1} and \nArray Two {result_arr2}.")
    elif choice == '4':
        result_arr1 = np.frompyfunc(dominicceiling, 1, 1)(arr1)
        result_arr2 = np.frompyfunc(dominicceiling, 1, 1)(arr2)
        print(f"\nCeiling values for Array One {result_arr1} and \nArray Two {result_arr2}.")
    elif choice == '5':
        result = np.frompyfunc(dominicsummation, 2, 1)(arr1, arr2)
        print(f"\nSummation result is {result}.")
    elif choice == '6':
        result_arr1 = np.frompyfunc(dominiccumulative_summation, 1, 1)(arr1)
        result_arr2 = np.frompyfunc(dominiccumulative_summation, 1, 1)(arr2)
        print(f"\nCumulative Summation result for Array One {result_arr1} and \nArray Two {result_arr2}.")

    # The user will have the choice to perform Rounding Decimals / Summation and Cumulative Summation
    while True:
        another_operation = get_user_input("\nDo you want to perform another operation? (yes/no): ").lower()
        if another_operation in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    if another_operation != 'yes':
        break