def calculate_deductions(gross_salary):
    tax_rate = 0.12
    tax = tax_rate * gross_salary

    #add validations

    while True:
        try:
            loan_amount = float(input("\nEnter the loan amount: "))
            break
        except ValueError:
            print("Please don't leave it blank/empty, put 0 if there is Loan")
    while True:
        try:
            insurance_amount = float(input("Enter the health insurance amount: "))
            break
        except ValueError:
            print("Please don't leave it blank/empty, put 0 if there is Insurance")

    total_deductions = tax + loan_amount + insurance_amount
    print(f"\nTax: Php {tax:,.2f}")
    print(f"Loan: Php {loan_amount:,.2f}")
    print(f"Insurance: Php {insurance_amount:,.2f}")
    print(f"Total Deductions: Php {total_deductions:,.2f}")
    return total_deductions

    #Copyrights © https://github.com/Dramos02