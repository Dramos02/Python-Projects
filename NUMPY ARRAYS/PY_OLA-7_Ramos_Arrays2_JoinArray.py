import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def get_user_input(message: object) -> object:
    while True:
        user_input = input(message)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please try again.")


arr1_input = get_user_input("Enter elements for Numpy Array 1 (comma-separated): ")
arr1 = np.array(list(map(int, arr1_input.split(','))))

arr2_input = get_user_input("Enter elements for Numpy Array 2 (comma-separated): ")
arr2 = np.array(list(map(int, arr2_input.split(','))))

arr = np.concatenate((arr1, arr2))
print("Concatenated array:", arr)