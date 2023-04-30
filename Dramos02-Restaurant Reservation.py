import re
#i imported regex for validate date and time

#i used class Reservation for OOP presentaion in python self.variable represents this like a Constructor
class Reservation:
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children

    #i used this as getter for subtotal in every reservation
    def get_subtotal(self):
        return self.adults * 500 + self.children * 300


#this class stores the every reservation acts like getters and setters
class ReservationSystem:
    def __init__(self):
        self.reservations = []

#this function view's all reserved data for a customer
    def view_All_Reservations(self):
        i_width = 5
        date_width = 25
        time_width = 25
        name_width = 40
        adults_width = 10
        children_width = 10
        #i research this to use this _width to specify the width so i can aligned it easily

        print(
            f"\n{'#':<{i_width}}Date{'':<{date_width - len('Date')}}Time{'':<{time_width - len('Time')}}Name{'':<{name_width - len('Name')}}Adults{'':<{adults_width - len('Adults')}}Children")
        for i, r in enumerate(self.reservations):
            print(
                f"{i + 1:<{i_width}}{r.date:<{date_width}}{r.time:<{time_width}}{r.name:<{name_width}}{str(r.adults):<{adults_width}}{str(r.children):<{children_width}}")

    def make_Reservation(self):
        while True:
            name = input("\nEnter name: ").title()
            if name:
                break
            print("\nPlease enter a valid Name")

        #name will validates if its empty and i used the .title() to capitalized every letter of the name

        while True:
            date = input("Enter Date (MMM DD, YYYY): ")
            if re.match(r'^[A-Z][a-z]{2,3} \d{1,2}, (19|20)\d{2}$|^[A-Z][a-z]{2,8} \d{1,2}, (19|20)\d{2}$', date):
                break
            print("\nPlease enter a valid Date (MMM DD, YYYY).")

            #i used regex to validate the formulation date, it only includes 3-Letter Abbreviation month as well as 4-Letter Abbreviation like June, July, Sept

        while True:
            time = input("Enter Time (HH:MM AM/PM): ").upper()
            if re.match(r'^((0?[1-9]|1[0-2]):([0-5][0-9]) ([AaPp][Mm]))$', time):
                break
            print("\nPlease enter a valid Time (HH:MM AM/PM).")

            #i used regex to validate the formulation of time, it doens't accepts military time like 13:00 - 23:59

        while True:
            try:
                adults = int(input("Enter number of adults: "))
                if adults < 1:
                    raise ValueError("\nValue should be greater than zero.")
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number 0 and negative number is not ACCEPTED.")

            #it will validates this if the user's input is absolute or real numbers.

        while True:
            try:
                children = int(input("Enter number of children: "))
                if children < 1:
                    raise ValueError("\nValue should be greater than zero.")
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number 0 and negative number is not ACCEPTED.")

                # it will validates this if the user's input is absolute or real numbers.

        reservation = Reservation(name, date, time, adults, children)
        self.reservations.append(reservation)
        self.save_reservations_to_file()
        print("\nReservation has been made and registered.")


    def delete_Reservation(self):
        while True:
            try:
                reservation_number = int(input("\nEnter reservation number to delete: "))
                if reservation_number < 1:
                    raise ValueError("Value should be greater than zero.")
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number 0 and negative number is not ACCEPTED.")

                # it will validates this if the user's input is absolute or real numbers.
        try:
            reservation = self.reservations.pop(reservation_number - 1)
            print(f"Reservation for {reservation.name} on {reservation.date} at {reservation.time} has been deleted.")
            self.save_reservations_to_file()
        except IndexError:
            print("\nSorry but your reservation not found.")

            #i used .pop to remove the row data of the number of being deleted

    def generate_Report(self):
        i_width = 1
        date_width = 20
        time_width = 20
        name_width = 35
        adults_width = 8
        children_width = 10
        subtotal_width = 10

        #i used it again _width to specify the width so i can aligned it easily
        print("\n" + "REPORT".center(106))
        print("#".ljust(i_width) + "\tDate".ljust(date_width) + "\tTime".ljust(time_width) +
              "\tName".ljust(name_width) + "Adults".ljust(adults_width) + "Children".ljust(children_width) +
              "Subtotal".ljust(subtotal_width))
        subtotal = 0
        total_adults = 0
        total_children = 0
        for i, r in enumerate(self.reservations):
            reservation_subtotal = r.adults * 500 + r.children * 300
            subtotal += reservation_subtotal
            total_adults += r.adults
            total_children += r.children
            print(
                f"{i + 1:{i_width}d}  {r.date.ljust(date_width)}{r.time.ljust(time_width)}{r.name.ljust(name_width)}{str(r.adults).ljust(adults_width)}{str(r.children).ljust(children_width)}{str(r.get_subtotal()).ljust(subtotal_width)}")

        print(f"\nTotal number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_children}")
        print(f"Grand Total: PHP {subtotal}")

    def save_reservations_to_file(self):

        with open("Reservations.txt", "w") as file:
            file.write("#\tName\t\t\tDate\t\tTime\t\tAdults\tChildren\tSubtotal\n")
            total_adults = 0
            total_kids = 0
            for i, r in enumerate(self.reservations, start=1):
                name_width = 25
                date_width = 15
                time_width = 15
                adults_width = 8
                children_width = 8
                subtotal_width = 10
                subtotal = r.adults * 500 + r.children * 300
                # i used it again _width to specify the width so i can aligned it easily
                file.write(
                    "{:<2d}\t{:<{name_width}}\t{:<{date_width}}\t{:<{time_width}}\t{:<{adults_width}}\t{:<{children_width}}\t{:<{subtotal_width}}\n".format(
                        i, r.name, r.date, r.time, r.adults, r.children, subtotal,
                        name_width=name_width, date_width=date_width, time_width=time_width,
                        adults_width=adults_width, children_width=children_width, subtotal_width=subtotal_width))
                total_adults += r.adults
                total_kids += r.children

            grand_total = total_adults * 500 + total_kids * 300
            file.write("\nTotal number of Adults: {}\n".format(total_adults))
            file.write("Total number of Kids: {}\n".format(total_kids))
            file.write("Grand Total: PHP {}\n".format(grand_total))

def main():
    system = ReservationSystem()
    while True:
        print("\nRestaurant Reservation Program by Dominic Ramos")
        print("\nSystem Menu")
        print("A. View all Reservations")
        print("B. Make Reservation")
        print("C. Delete Reservation")
        print("D. Generate Report")
        print("E. Exit")

        choice = input("Enter your choice: ")

        try:
            # i used or here so user can choose from [a-d/A-D]
            if choice == "a" or choice == "A":
                system.view_All_Reservations()
            elif choice == "b" or choice == "B":
                system.make_Reservation()
            elif choice == "c" or choice == "C":
                system.delete_Reservation()
            elif choice == "d" or choice == "D":
                system.generate_Report()
            elif choice == "e" or choice == "E":
                print("\nThank you for using My Restaurant Reservation Program")
                break
            else:
                raise ValueError("Invalid choice. Please choose from [a-d/A-D].")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

    #this will act's like an main class like in OOP in Java
    #Copyrights © https://github.com/Dramos02