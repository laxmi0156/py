class BusReservation:
    def __init__(self):
        # predefined routes with prices
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 700,
            "Kolkata to Durgapur": 450
        }

        self.tickets = {}      # ticket_id : ticket_details
        self.seat_count = {}   # route : booked seats
        self.ticket_id = 10000

        for route in self.routes:
            self.seat_count[route] = 0

    def show_routes(self):
        print("\n--- Available Routes ---")
        for route, price in self.routes.items():
            print(f"{route} - ₹{price}")

    def book_ticket(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")

        self.show_routes()
        route = input("Select route: ")

        if route not in self.routes:
            print("Invalid route.")
            return

        if self.seat_count[route] >= 40:
            print("No seats available on this route.")
            return

        self.ticket_id += 1
        self.seat_count[route] += 1

        self.tickets[self.ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "price": self.routes[route],
            "seat": self.seat_count[route]
        }

        print("\nTicket booked successfully!")
        print("Ticket ID:", self.ticket_id)
        print("Seat No:", self.seat_count[route])

    def view_ticket(self):
        tid = int(input("Enter ticket ID: "))

        if tid in self.tickets:
            t = self.tickets[tid]
            print("\n--- Ticket Details ---")
            print("Name:", t["name"])
            print("Age:", t["age"])
            print("Mobile:", t["mobile"])
            print("Route:", t["route"])
            print("Seat No:", t["seat"])
            print("Price: ₹", t["price"])
        else:
            print("Ticket not found.")

    def cancel_ticket(self):
        tid = int(input("Enter ticket ID to cancel: "))

        if tid in self.tickets:
            route = self.tickets[tid]["route"]
            del self.tickets[tid]
            self.seat_count[route] -= 1
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found.")

    def menu(self):
        while True:
            print("\n--- Bus Reservation System ---")
            print("1. Show Available Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.show_routes()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_ticket()
            elif choice == "4":
                self.cancel_ticket()
            elif choice == "5":
                print("Thank you! Visit again.")
                break
            else:
                print("Invalid choice.")

bus = BusReservation()
bus.menu()
