import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


# validation
def get_user_input(message):
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Field cannot be empty. Please try again.")


array_input = get_user_input("Enter space-separated string values for the array: ")

# string - integer
user_input_values = [int(num) for num in array_input.split()]

arr = np.array(user_input_values)
print("Original Array:", arr)

index_input = get_user_input("\nEnter the index value to be viewed: ")

try:
    # Convert the user input index into an integer
    index_value = int(index_input)
except ValueError:
    print("Error: Invalid input for the index value. Please enter a valid integer.")
    exit()

value_input = get_user_input("Enter the value to modify the original array: ")

try:
    # Convert the user input value into an integer
    value_to_modify = int(value_input)
except ValueError:
    print("Error: Invalid input for the modification value. Please enter a valid integer.")
    exit()

arr[index_value] = value_to_modify
view_value = arr.view()

print("Viewed Array:", view_value)
