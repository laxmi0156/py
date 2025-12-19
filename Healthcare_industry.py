class ClinicAppointment:
    def __init__(self):
        # appointments stored as:
        # { mobile: {details} }
        self.appointments = {}

        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.max_per_slot = 3

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        mobile = int(input("Enter mobile number: "))
        doctor = input("Enter preferred doctor name: ")

        print("\nAvailable Time Slots:")
        for slot in self.time_slots:
            print(slot)

        slot = input("Choose time slot: ")

        if slot not in self.time_slots:
            print("Invalid time slot!")
            return

        # Count existing appointments for same doctor & slot
        count = 0
        for appt in self.appointments.values():
            if appt["doctor"] == doctor and appt["slot"] == slot:
                count += 1

        if count >= self.max_per_slot:
            print("Slot full for this doctor. Choose another slot.")
            return

        self.appointments[mobile] = {
            "name": name,
            "age": age,
            "doctor": doctor,
            "slot": slot
        }

        print("Appointment booked successfully!")

    def view_appointment(self):
        mobile = int(input("Enter mobile number: "))

        if mobile in self.appointments:
            appt = self.appointments[mobile]
            print("\n--- Appointment Details ---")
            print("Name:", appt["name"])
            print("Age:", appt["age"])
            print("Doctor:", appt["doctor"])
            print("Time Slot:", appt["slot"])
        else:
            print("No appointment found.")

    def cancel_appointment(self):
        mobile = input("Enter mobile number: ")

        if mobile in self.appointments:
            del self.appointments[mobile]
            print(" Appointment cancelled.")
        else:
            print("No appointment found.")

    def menu(self):
        while True:
            print("\n--- Clinic Appointment System ---")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointment()
            elif choice == "3":
                self.cancel_appointment()
            elif choice == "4":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

clinic = ClinicAppointment()
clinic.menu()


                