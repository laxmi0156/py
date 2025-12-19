class SchoolManagement:
    def __init__(self):
        self.students = {}        # stores student records
        self.student_id = 1000    # starting ID

    def new_admission(self):
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        std_class = int(input("Enter class (1-12): "))
        mobile = input("Enter guardian mobile number: ")

        # Age validation
        if age < 5 or age > 18:
            print("Age must be between 5 and 18.")
            return

        # Mobile validation
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Mobile number must be 10 digits.")
            return

        # Class validation
        if std_class < 1 or std_class > 12:
            print("Class must be between 1 and 12.")
            return

        self.student_id += 1

        self.students[self.student_id] = {
            "name": name,
            "age": age,
            "class": std_class,
            "mobile": mobile
        }

        print(f"Admission successful! Student ID: {self.student_id}")

    def view_student(self):
        sid = int(input("Enter student ID: "))

        if sid in self.students:
            s = self.students[sid]
            print("\n--- Student Details ---")
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Class:", s["class"])
            print("Mobile:", s["mobile"])
        else:
            print("Student not found.")

    def update_student(self):
        sid = int(input("Enter student ID: "))

        if sid not in self.students:
            print("Student not found.")
            return

        print("1. Update Mobile Number")
        print("2. Update Class")
        choice = input("Enter choice: ")

        if choice == "1":
            mobile = input("Enter new mobile number: ")
            if mobile.isdigit() and len(mobile) == 10:
                self.students[sid]["mobile"] = mobile
                print("Mobile number updated.")
            else:
                print("Invalid mobile number.")

        elif choice == "2":
            std_class = int(input("Enter new class (1-12): "))
            if 1 <= std_class <= 12:
                self.students[sid]["class"] = std_class
                print("Class updated.")
            else:
                print("Invalid class.")

        else:
            print("Invalid choice.")

    def remove_student(self):
        sid = int(input("Enter student ID to remove: "))

        if sid in self.students:
            del self.students[sid]
            print("Student record removed.")
        else:
            print("Student not found.")

    def menu(self):
        while True:
            print("\n--- School Management System ---")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.new_admission()
            elif choice == "2":
                self.view_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.remove_student()
            elif choice == "5":
                print("Thank you! Exiting system.")
                break
            else:
                print(" Invalid choice.")
                break

school = SchoolManagement()
school.menu()
