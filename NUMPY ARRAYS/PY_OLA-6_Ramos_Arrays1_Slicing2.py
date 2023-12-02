import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

# validation
while True:
    array_input = input("Enter space-separated (ex.1 2 3) values for the array: ")

    # validate
    if array_input.strip():
        #string - integer
        user_input_values = [int(num) for num in array_input.split()]
        break
    else:
        print("Array values cannot be empty. Please try again.")

# np.array
arr = np.array(user_input_values)

# code snipper slicing example 2
while True:
    slicing_input = input("Enter the slicing expression (e.g., arr[4:]): ")

    # Validate that the input is not empty
    if slicing_input.strip():
        try:
            # Use eval to evaluate the user input as a Python expression
            sliced_array = eval(f"arr{'' if slicing_input.startswith('[') else '.'}{slicing_input}")
            print(f"Sliced array using expression '{slicing_input}': {sliced_array}")
            break
        except Exception as e:
            print(f"{e}. Please enter a valid slicing expression.")
    else:
        print("Slicing expression cannot be empty. Please try again.")
