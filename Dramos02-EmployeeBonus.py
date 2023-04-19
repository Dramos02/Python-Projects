print("Please answer the following to check your Bonus based on your Years in Service and Department Code.")
employeeName = str(input("\nEnter your name: "))
while True:
    serviceYear = int(input("Enter your Year-in-Service: "))
    if serviceYear <= 0:
        print("Please enter atleast 1 year for your Year-in-Service")
    else:
        break
deptCode = ("IT", "Acct", "HR")
employeeCode = None
employeeBonus = 0
while employeeCode not in deptCode:
    employeeCode = str(input("Enter your Department Code: ")).upper()
    if employeeCode == "IT":
        if serviceYear >= 10:
            employeeBonus = 10000
        elif serviceYear <= 9:
            employeeBonus = 5000
        break
    elif employeeCode == "ACCT":
        if serviceYear >= 10:
            employeeBonus = 10000
        elif serviceYear <= 9:
            employeeBonus = 5000
        break
    elif employeeCode == "HR":
        if serviceYear >= 10:
            employeeBonus = 10000
        elif serviceYear <= 9:
            employeeBonus = 5000
        break
    else:
        print("Please CHOOSE ONLY FROM THE FOLLOWING DEPARTMENT CODE [IT] [Acct] [HR]")

print("Hi " + employeeName + ", your bonus is " + "{}".format(employeeBonus))


"""
copyright @ https://github.com/Dramos02
"""