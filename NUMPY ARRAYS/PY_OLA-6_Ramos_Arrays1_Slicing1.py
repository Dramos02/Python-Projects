import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")

# validation
while True:
    array_input = input("Enter space-separated (ex.1 2 3) values for the array: ")

    # validation
    if array_input.strip():
        #string - integer
        user_input_values = [int(num) for num in array_input.split()]
        break
    else:
        print("Array values cannot be empty. Please try again.")

# np.array
arr = np.array(user_input_values)

# validation
while True:
    start_index_input = input("Enter the start index: ")
    end_index_input = input("Enter the end index: ")

    # validation
    if start_index_input.lstrip('-').isdigit() and end_index_input.lstrip('-').isdigit():
        start_index = int(start_index_input)
        end_index = int(end_index_input)

        # slicing
        sliced_array = arr[start_index:end_index]

        print(f"Sliced array from index {start_index} to {end_index - 1}: {sliced_array}")
        break
    else:
        print("Error: Please enter valid integers for the start and end indices.")


