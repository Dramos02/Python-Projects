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


values_input = get_user_input("Enter space-separated values for the array: ")

try:
    values = [int(num) for num in values_input.split()]
except ValueError:
    print("Error: Invalid input for array values. Please enter valid integers.")
    exit()

arr = np.array(values)

while True:
    search_input = get_user_input("Enter the element to search: ")

    try:
        search_element = int(search_input)
    except ValueError:
        print("Error: Invalid input for the element to search. Please enter a valid integer.")
        continue

    indices = np.where(arr == search_element)

    #  Added validation it will loop till the element entered is existing from the Numpy Array
    if indices[0].size > 0:
        print(f"\nIndices where {search_element} occurs in the array: {indices}")
        break
    else:
        print(f"{search_element} is not in the array. Please enter a valid value.")