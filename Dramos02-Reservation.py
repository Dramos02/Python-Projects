# Provides access to some variables and functions that interact with the Python interpreter.
import sys
import re


# Reservation which represents a reservation for a restaurant
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
        print("\nRESTAURANT RESERVATION SYSTEM")
        print("System Menu")
        print("a/A. View all Reservations")
        print("b/B. Make Reservation")
        print("c/C. Delete Reservation")
        print("d/D. Generate Report")
        print("e/E. Exit")

        choice = input("Enter your choice: ").lower()

        try:
            if choice.lower() == "a":
                system.view_all_reservations()
            elif choice.lower() == "b":
                system.make_reservation()
            elif choice.lower() == "c":
                system.delete_reservation()
            elif choice.lower() == "d":
                system.generate_report()
            elif choice.lower() == "e":
                print("Thank you!")
                sys.exit()
            else:
                raise ValueError("Invalid choice. Please enter a valid option (a-e).")
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
        print("\n# Date\t\t\t\t\tTime\t\t\t\tName\t\t\t\t\t\t\tAdults\t\tChildren")
        for i, r in enumerate(self.reservations):
            print(
                f"{i + 1} {r.date.ljust(20)}{r.time.ljust(20)}{r.name.ljust(34)}{str(r.adults).ljust(12)}{str(r.children)}")

    # Reservation Maker
    def make_reservation(self):
        while True:
            name = input("\nEnter name: ")
            if name:
                break
            print("Please enter A Name")

        while True:
            date = input("Enter Date (MMM DD, YYYY): ")
            if re.match(r'^[A-Z][a-z]{2,3} \d{1,2}, (19|20)\d{2}$|^[A-Z][a-z]{2,8} \d{1,2}, (19|20)\d{2}$', date):
                break
            print("Please enter a valid Date (MMM DD, YYYY).")

        while True:
            time = input("Enter Time (HH:MM AM/PM): ")
            if re.match(r'^((0?[1-9]|1[0-2]):([0-5][0-9]) ([AaPp][Mm]))$', time):
                break
            print("Please enter a valid Time (HH:MM AM/PM).")

        adults = get_integer_input("Enter number of Adults: ")
        children = get_integer_input("Enter number of Children: ")

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
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tREPORT")
        print("#  Date\t\t\t\t\tTime\t\t\t\tName\t\t\t\t\t\t\tAdults\tChildren\tSubtotal")
        subtotal = 0
        total_adults = 0
        total_children = 0
        for i, r in enumerate(self.reservations):
            subtotal += r.get_subtotal()
            total_adults += r.adults
            total_children += r.children
            print(
                f"{i + 1:2d}  {r.date.ljust(20)}{r.time.ljust(20)}{r.name.ljust(35)}{str(r.adults).ljust(8)}{str(r.children).ljust(10)}{str(r.get_subtotal()).ljust(10)}")

        print(f"\nTotal number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_children}")
        print(f"Grand Total: PHP {subtotal}")

# Saving the File to Reservations.txt
    def save_reservations_to_file(self):
        """with open("Reservations.txt", "w") as file:
            file.write("\nName\t\t\tDate\t\t\t\t\tTime\t\t\t\t\tAdults\t\t\t\t\tChildren\t\t\t\tSubtotal\n")
            total_adults = 0
            total_kids = 0
            for r in self.reservations:
                file.write(f"{r.name}\t\t\t{r.date}\t\t\t\t{r.time}\t\t\t\t{r.adults}\t\t\t\t{r.children}\t\t\t\t{r.get_subtotal()}\n")
                total_adults += r.adults
                total_kids += r.children
            grand_total = total_adults * 500 + total_kids * 300
            file.write(f"\nTotal number of Adults: {total_adults}\n")
            file.write(f"Total number of Kids: {total_kids}\n")
            file.write(f"Grand Total: PHP {grand_total}\n")
        """
        with open("Reservations.txt", "w") as file:
            file.write("Name\t\t\t\t\t\tDate\t\t\tTime\t\t\tAdults\t\tChildren\tSubtotal\n")
            total_adults = 0
            total_kids = 0
            for r in self.reservations:
                name_width = 25
                date_width = 15
                time_width = 15
                adults_width = 8
                children_width = 8
                subtotal_width = 10
                file.write(
                    "{:<{name_width}}\t{:<{date_width}}\t{:<{time_width}}\t{:<{adults_width}}\t{:<{children_width}}\t{:<{subtotal_width}}\n".format(
                        r.name, r.date, r.time, r.adults, r.children, r.get_subtotal(),
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
