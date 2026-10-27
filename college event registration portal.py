# College Event Registration Portal

# events = [
    
#     ["101", "Tech Fest", "20-08-2026", "Main Auditorium", 50],
#     ["102", "Cultural Fest", "25-08-2026", "College Ground", 100],
#     ["103", "Sports Meet", "30-08-2026", "Sports Complex", 75]
# ]

# registrations = []

# def view_events():
#     print("\n========== AVAILABLE EVENTS ==========")
    
#     for event in events:
#         print("\nEvent ID   :", event[0])
#         print("Event Name :", event[1])
#         print("Date       :", event[2])
#         print("Venue      :", event[3])
#         print("Seats Left :", event[4])
#         print("--------------------------------------")


# def register_event():
#     view_events()

#     event_id = input("\nEnter Event ID to register: ")

#     found = False

#     for event in events:
#         if event[0] == event_id:
#             found = True

#             if event[4] > 0:
#                 name = input("Enter Student Name: ")
#                 roll_no = input("Enter Roll Number: ")

#                 registrations.append([name, roll_no, event[1]])

#                 event[4] = event[4] - 1

#                 print("\nRegistration Successful!")
#                 print("Student :", name)
#                 print("Event   :", event[1])
#                 print("Seats Remaining :", event[4])

#             else:
#                 print("\nSorry! No seats available.")

#             break

#     if found == False:
#         print("\nInvalid Event ID!")


# while True:

#     print("\n======================================")
#     print("   COLLEGE EVENT REGISTRATION PORTAL")
#     print("======================================")
#     print("1. View All Events")
#     print("2. Register for Event")
#     print("3. Exit")
#     print("======================================")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         view_events()

#     elif choice == "2":
#         register_event()

#     elif choice == "3":
#         print("\nThank you for using the portal!")
#         break

#     else:
#         print("\nInvalid choice! Please try again.")

class Student:
    def _init_(self):
        self.name = input("Enter Name: ")
        self.reg_no = input("Enter Registration Number: ")
        self.marks = []

        for i in range(5):
            mark = int(input(f"Enter Marks in Subject {i+1}: "))
            self.marks.append(mark)

    def calculate_result(self):
        self.total = sum(self.marks)
        self.percentage = self.total / 5

        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Registration Number:", self.reg_no)
        print("Total Marks:", self.total)
        print("Percentage:", self.percentage)
        print("Grade:", self.grade)

s = Student()
s.calculate_result()
s.display()