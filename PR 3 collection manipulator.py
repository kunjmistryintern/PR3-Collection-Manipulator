# PR3 Collection Manipulator
# Name Kunj Mistry
# GR ID : 12078
# Batch : RW6
# Date : 13/11/25

print("Welcome to the student organizer!")
students = []
while True:
     print ("Select an option:")
     print(" ")
     print("1. Add Student")
     print("2. Display All Students")
     print("3. Update Student Infomation")
     print("4. Delete Student")
     print("5. Subject Offered")
     print("6. Exit")
     print(" ")
     
     choice = int(input("Enter your choice (1-6): "))
     print(" ")

     match choice:
         
        case 1:
            
            print(" ")
            print ("You have choice option 1: Add Student")
            print(" ")
            id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            bod = input("Enter Student Birth Date (DD/MM/YYYY) : ")
            subject = input("Enter Student Subjects (comma-separated): ").strip()
            sub = [s.strip() for s in subject.split(",") if s.strip()]  


            students.append({"id": id, "name": name, "age": age, "grade": grade, "bod": bod,"id_bod": (id, bod),"subject": sub})
            print(" ")
            print(f"Student {name} added successfully.")
            print(" ")

        case 2:
                
            print ("You have choice option 2: Display All Students")   
            print(" ")
            if not students:
                print("No students to display.")
            else:
                for s in students:
                    print(f"ID: {s['id']}")
                    print(f"Name: {s['name']}")
                    print(f"Age: {s['age']}")
                    print(f"Grade: {s['grade']}")
                    print(f"BOD: {s['bod']}")
                    print(f"Subjects: {s['subject']}")
                    print("")

            print(" ")
        
        case 3:

            print ("You have choice option 3: Update Student Infomation")
            print(" ")
            upid = input("Enter ID to update:")  

            student = None
            for s in students:
                if str(s["id"]) == upid:
                    student = s
                    break

            if student is None:
                print(f"No student found with ID {upid}.")
                print(" ")
                continue

            new_name = input(f"Enter new name:")
            if new_name:
                student['name'] = new_name

            new_age = input(f"Enter new age:")
            if new_age:
                student['age'] = new_age

            new_grade = input(f"Enter new grade:")
            if new_grade:
                student['grade'] = new_grade

            new_subjects = input("Enter new subjects (comma-separated):")
            if new_subjects:
                student['subject'] = [x for x in new_subjects.split(",") if x]

            print(" ")
            print(f"Student ID {upid} updated (ID and Date of birth will not be changed).")
            print(" ")
            
        case 4:
            print ("You have choice option 4: Delete Student")
            print(" ")
            a=input('enter student id ')
            for s in students:
                if str(s["id"]) == a:
                    students.remove(s)
                    print(" ")
                    print(f"Student with ID {a} has been deleted.")
                    break
            print(" ")

        case 5:
            print ("You have choice option 5: Subject Offered")
            print(" ")

            for student in students:
                print("Subject Offered:")
                for sub in student.get("subject", []):
                    
                    print( sub)
            print(" ")
            
        case 6:
            print ("Exiting the program. Goodbye!")
            break

