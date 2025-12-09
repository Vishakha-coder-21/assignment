class HotelReservation:
    def __init__(self):
        self.booking = None

    def book_room(self):
        if self.booking is not None:
            print("You already have a booking. View/Cancel it first.\n")
            return

        name = input("Enter your name: ")
        contact = input("Enter 10-digit contact number: ")

        if not (contact.isdigit() and len(contact) == 10):
            print("Invalid contact number!\n")
            return

        nights = int(input("Enter number of nights: "))

        print("\nRoom Types:")
        print("1. Standard - 2000/night")
        print("2. Deluxe - 3500/night")
        print("3. Suite - 5000/night")

        choice = int(input("Choose room type (1/2/3): "))

        if choice == 1:
            room = "Standard"
            cost = 2000
        elif choice == 2:
            room = "Deluxe"
            cost = 3500
        elif choice == 3:
            room = "Suite"
            cost = 5000
        else:
            print("Invalid choice!\n")
            return

        total = cost * nights
        print(f"\nTotal cost = {total}")

        confirm = input("Confirm booking? (yes/no): ").lower()

        if confirm == "yes":
            self.booking = {
                "Name": name,
                "Contact": contact,
                "Room Type": room,
                "Nights": nights,
                "Total Cost": total
            }
            print("\nBooking Successful!\n")
        else:
            print("Booking not confirmed.\n")

    def view_booking(self):
        if self.booking is None:
            print("No booking found.\n")
        else:
            print("\n--- Booking Details ---")
            for key, value in self.booking.items():
                print(key, ":", value)
            print()

    def cancel_booking(self):
        if self.booking is None:
            print("No booking to cancel.\n")
        else:
            confirm = input("Cancel booking? (yes/no): ").lower()
            if confirm == "yes":
                self.booking = None
                print("Booking cancelled.\n")
            else:
                print("Cancellation aborted.\n")

    def menu(self):
        while True:
            print("1. Book Room")
            print("2. View Booking")
            print("3. Cancel Booking")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.book_room()
            elif choice == 2:
                self.view_booking()
            elif choice == 3:
                self.cancel_booking()
            elif choice == 4:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!\n")


hotel = HotelReservation()
hotel.menu()
