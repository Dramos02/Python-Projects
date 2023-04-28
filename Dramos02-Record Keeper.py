import re
#i imported regex for my email address to validate

def add_Record():
    print("RECORD KEEPING APP BY DOMINIC RAMOS:\n")
    #i used while for every validation is it will keep on checking until user satisfied the validaiton
    while True:
        #i use try catch for file handling and to get ValueError
        try:
            name = input("Enter your name: ")
            while not name:
                name = input("\nName cannot be empty, Please Try Again \nEnter your name: ")

            email = input("Enter your email address: ")
            while not email:
                email = input("\nEmail cannot be empty, Please Try Again \nEnter your email: ")
          #this is the simple regex where in user should put @on their email address just the usual format
            while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                email = input("\nInvalid email address format. \nEnter a valid email: ")

            address = input("Enter your home address: ")
            while not address:
                address = input("\nAddress cannot be empty, Please Try Again \nEnter your address: ")

            with open("records.txt", "a") as file:
                file.write(f"\nName: {name} \nEmail: {email} \nAddress {address}\n")
            print("Record added successfully!\n")

            break
        except ValueError as e:
            print(f"Invalid input: {str(e)}\nPlease try again.\n")


def view_Records():
    #this try catch will read all lines from records.txt then it will printed out by for loop using strip
    try:
        with open("records.txt", "r") as file:
            records = file.readlines()
            if len(records) == 0:
                print("No records found!")
            else:
                for record in records:
                    print(record.strip())
    except FileNotFoundError:
        print("No records found!\n")

def clear_Records():
    #this is how file handling will clear data by using w
    try:
        with open("records.txt", "w") as file:
            print("The Record File is cleared successfully!")
    except FileNotFoundError:
        print("No records found!\n")


#this is the main of the Record Keeping on handling user's choices
while True:
    print("\nRECORD KEEPING APP BY DOMINIC RAMOS:")
    print("A. Add a Record")
    print("B. View All Records")
    print("C. Clear All Records")
    print("D. Exit")

    choice = input("Enter your choice: ")
    #i used or here so user can choose from [a-d/A-D]
    if choice == "a" or choice == "A" :
        add_Record()
    elif choice == "b" or choice == "B":
        view_Records()
    elif choice == "c" or choice == "C":
        clear_Records()
    elif choice == "d" or choice == "D":
        print("Thank you for using Recording Keeper by Dominic Ramos")
        break
    else:
        print("Invalid choice. Please choose from [a-d/A-D].")

    #Copyrights © https://github.com/Dramos02