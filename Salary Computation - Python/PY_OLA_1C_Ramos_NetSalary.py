import PY_OLA_1A_Ramos_Salary as module_Salary
import PY_OLA_1B_Ramos_Deductions as module_Deductions

#i use "import" to use other module and rename it with the use of "as"

def calculate_net_salary():
    while True:
        gross_salary = module_Salary.calculate_gross_salary()
        total_deductions = module_Deductions.calculate_deductions(gross_salary)
        net_salary = gross_salary - total_deductions
        print(f"\nNet Salary: Php {net_salary:,.2f}")

        # add validations
        while True:
            another_employee = input("\nDo you want to input data for another employee? (yes/no): ").lower()
            if another_employee == "yes" or another_employee == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no' only.")

        # add validations
        if another_employee != "yes":
            print("\nThank you for using Salary Computation programmed by Ramos, Dominic O.")
            break
        else:
            print("\n")


calculate_net_salary()

    #Copyrights © https://github.com/Dramos02