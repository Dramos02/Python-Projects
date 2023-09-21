def calculate_gross_salary():
    # add validations
    while True:
        name = input("Enter employee name: ")
        if name.strip() == "":
            print("Employee name cannot be empty. Please enter a valid name.")
        else:
            break

    while True:
        try:
            hours_worked = float(input("Enter the number of hours worked: "))
            if hours_worked <= 0:
                print("Hours worked must be greater than 0. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for hours worked.")

    hourly_rate = 500.00
    gross_salary = hourly_rate * hours_worked
    print(f"\nThis Salary Computation for \n{name.title()}")
    print(f"Hour: {hours_worked:.2f} HRS")
    print(f"Gross Salary: Php {gross_salary:,.2f}")
    return gross_salary

    # Copyrights © https://github.com/Dramos02