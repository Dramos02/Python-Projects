def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y


while True:
    print("Basic Calculator App"
          "\nEnter 'add' for addition"
          "\nEnter 'subtract' for subtraction "
          "\nEnter 'multiply' for multiplication"
          "\nEnter 'divide' for division")

    #add validition

    while True:
        user_input = input("\nCalculation Option: ").lower()
        if user_input in ["add", "subtract", "multiply", "divide"]:
            break
        else:
            print("Invalid input. Please choose 'add,' 'subtract,' 'multiply,' or 'divide'.")

    while True:
        try:
            num1_str = input("Enter first number: ")
            if not num1_str:
                print("Error: First number cannot be empty.")
                continue
            num1 = float(num1_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num2_str = input("Enter second number: ")
            if not num2_str:
                print("Error: Second number cannot be empty.")
                continue
            num2 = float(num2_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    try:
        if user_input == "add":
            print("Result:", addition(num1, num2))
        elif user_input == "subtract":
            print(f"Result:", subtraction(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiplication(num1, num2))
        elif user_input == "divide":
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            else:
                print("Result:", division(num1, num2))

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

    except ZeroDivisionError as e:
        print(e)

    while True:
        another_calculation = input("\nDo you want to perform another calculation (yes/no): ").lower()
        if another_calculation == "yes" or another_calculation == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no' only.")

    if another_calculation != "yes":
        print("\nThank you for using Basic Calculator App programmed by Ramos, Dominic O.")
        break
    else:
        print("\n")

    #Copyrights © https://github.com/Dramos02