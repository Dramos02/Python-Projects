def add_record():
    print("RECORD KEEPING APP BY DOMINIC RAMOS:\n")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    address = input("Enter your home address: ")
    with open("records.txt", "a") as file:
        file.write(f"\nName: {name} \nEmail: {email} \nAddress {address}\n")
    print("Record added successfully!\n")

def view_records():
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

def clear_records():
    try:
        with open("records.txt", "w") as file:
            print("The Record File is cleared successfully!")
    except FileNotFoundError:
        print("No records found!\n")

while True:
    print("\nRECORD KEEPING APP BY DOMINIC RAMOS:")
    print("A. Add a Record")
    print("B. View All Records")
    print("C. Clear All Records")
    print("D. Exit")

    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A" :
        add_record()
    elif choice == "b" or choice == "B":
        view_records()
    elif choice == "c" or choice == "C":
        clear_records()
    elif choice == "d" or choice == "D":
        print("Thank you for using Recording Keeper by Dominic Ramos")
        break
    else:
        print("Invalid choice. Please choose from [a-d/A-D].")