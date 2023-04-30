import re


class Reservation:
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children

    # Get_subtotal method calculates and returns the subtotal for the reservation based on the number of adults and children.
    def get_subtotal(self):
        return self.adults * 500 + self.children * 300


# Main Command-line interface for a restaurant reservation system.
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
            if choice == "a" or choice == "A":
                system.view_all_reservations()
            elif choice == "b" or choice == "B":
                system.make_reservation()
            elif choice == "c" or choice == "C":
                system.delete_reservation()
            elif choice == "d" or choice == "D":
                system.generate_report()
            elif choice == "e" or choice == "E":
                print("Thank you for using My Restaurant Reservation Program")
            else:
                raise ValueError("Invalid choice. Please choose from [a-d/A-D].")
        except Exception as e:
            print(f"Error: {e}")


# Validation for the Number of Adults And Children
def get_integer_input(message):
    while True:
        try:
            value = int(input(message))
            if value < 1:
                raise ValueError("Value should be greater than zero.")
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number greater than zero.")


# Store instances of the Reservation
class ReservationSystem:
    def __init__(self):
        self.reservations = []

# View All the Reservations Available
    def view_all_reservations(self):
        i_width = 5
        date_width = 25
        time_width = 25
        name_width = 40
        adults_width = 10
        children_width = 10

        print(
            f"\n{'#':<{i_width}}Date{'':<{date_width - len('Date')}}Time{'':<{time_width - len('Time')}}Name{'':<{name_width - len('Name')}}Adults{'':<{adults_width - len('Adults')}}Children")
        for i, r in enumerate(self.reservations):
            print(
                f"{i + 1:<{i_width}}{r.date:<{date_width}}{r.time:<{time_width}}{r.name:<{name_width}}{str(r.adults):<{adults_width}}{str(r.children):<{children_width}}")

    # Reservation Maker
    def make_reservation(self):
        while True:
            name = input("\nEnter name: ").title()
            if name:
                break
            print("Please enter A Name")

        while True:
            date = input("Enter Date (MMM DD, YYYY): ")
            if re.match(r'^[A-Z][a-z]{2,3} \d{1,2}, (19|20)\d{2}$|^[A-Z][a-z]{2,8} \d{1,2}, (19|20)\d{2}$', date):
                break
            print("Please enter a valid Date (MMM DD, YYYY).")

        while True:
            time = input("Enter Time (HH:MM AM/PM): ").upper()
            if re.match(r'^((0?[1-9]|1[0-2]):([0-5][0-9]) ([AaPp][Mm]))$', time):
                break
            print("Please enter a valid Time (HH:MM AM/PM).")

        while True:
            try:
                adults = int(input("Enter number of adults: "))
                if adults < 1:
                    raise ValueError("Value should be greater than zero.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number greater than zero.")

        while True:
            try:
                children = int(input("Enter number of children: "))
                if children < 0:
                    raise ValueError("Value should be greater than or equal to zero.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number greater than or equal to zero.")

        reservation = Reservation(name, date, time, adults, children)
        self.reservations.append(reservation)
        self.save_reservations_to_file()
        print("Reservation has been made.")

# Deletion of a User based on the Number Inserted using ".pop" Method
    def delete_reservation(self):
        try:
            reservation_number = get_integer_input("\nEnter reservation number to delete: ")
            reservation = self.reservations.pop(reservation_number - 1)
            print(f"Reservation for {reservation.name} on {reservation.date} at {reservation.time} has been deleted.")
            self.save_reservations_to_file()
        except IndexError:
            print("Reservation not found.")

# Generation of the Report
    def generate_report(self):
        i_width = 1
        date_width = 20
        time_width = 20
        name_width = 35
        adults_width = 8
        children_width = 10
        subtotal_width = 10

        print("\n" + "REPORT".center(106))
        print("#".ljust(i_width) + "\tDate".ljust(date_width) + "\tTime".ljust(time_width) +
              "\tName".ljust(name_width) + "Adults".ljust(adults_width) + "Children".ljust(children_width) +
              "Subtotal".ljust(subtotal_width))
        subtotal = 0
        total_adults = 0
        total_children = 0
        for i, r in enumerate(self.reservations):
            subtotal += r.get_subtotal()
            total_adults += r.adults
            total_children += r.children
            print(
                f"{i + 1:{i_width}d}  {r.date.ljust(date_width)}{r.time.ljust(time_width)}{r.name.ljust(name_width)}{str(r.adults).ljust(adults_width)}{str(r.children).ljust(children_width)}{str(r.get_subtotal()).ljust(subtotal_width)}")

        print(f"\nTotal number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_children}")
        print(f"Grand Total: PHP {subtotal}")

# Saving the File to Reservations.txt
    def save_reservations_to_file(self):

        with open("Reservations.txt", "w") as file:
            file.write("#\tName\t\t\t\t\t\tDate\t\t\tTime\t\t\tAdults\t\tChildren\tSubtotal\n")
            total_adults = 0
            total_kids = 0
            for i, r in enumerate(self.reservations, start=1):
                name_width = 25
                date_width = 15
                time_width = 15
                adults_width = 8
                children_width = 8
                subtotal_width = 10
                file.write(
                    "{:<2d}\t{:<{name_width}}\t{:<{date_width}}\t{:<{time_width}}\t{:<{adults_width}}\t{:<{children_width}}\t{:<{subtotal_width}}\n".format(
                        i, r.name, r.date, r.time, r.adults, r.children, r.get_subtotal(),
                        name_width=name_width, date_width=date_width, time_width=time_width,
                        adults_width=adults_width, children_width=children_width, subtotal_width=subtotal_width))
                total_adults += r.adults
                total_kids += r.children
            grand_total = total_adults * 500 + total_kids * 300
            file.write("\nTotal number of Adults: {}\n".format(total_adults))
            file.write("Total number of Kids: {}\n".format(total_kids))
            file.write("Grand Total: PHP {}\n".format(grand_total))
if __name__ == "__main__":
    main()
