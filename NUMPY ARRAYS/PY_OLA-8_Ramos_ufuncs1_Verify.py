import numpy as np

print("Dominic O. Ramos " +
      "\n 3-BSIT-2")


def check_ufunc(func):
    if type(func) == np.ufunc:
        print(f'{func.__name__} is a ufunc')
    else:
        print(f'{func.__name__} is not a ufunc')


while True:
    func_name = input("Enter a NumPy function name (e.g., add): ")

    try:
        numpy_func = getattr(np, func_name)
    except AttributeError:
        print(f"Error: '{func_name}' is not a valid NumPy function. Please try again.")
    else:
        # Check if the function is a ufunc
        check_ufunc(numpy_func)
        break  # Exit the loop if a valid function is entered
