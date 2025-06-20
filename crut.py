# Global list to store student records
students = []

# Function to validate that the entered name is not a number
def validate_name_input(name_to_validate):
    while name_to_validate.isdigit():  # Check if the name is a number
        name_to_validate = input("Please enter a valid name: ")
    while " " in name_to_validate:  # Check if the name contains spaces
        name_to_validate = input("Please enter a name without spaces: ")
    return name_to_validate

# Function to validate that the input is a number
def validate_number_input(number_to_validate):
    while not number_to_validate.isdigit():  # Check if the input is not a number
        number_to_validate = input("Please enter only numbers: ")
    return number_to_validate

# Main program loop
option = ""
while option != "6":
    # Display menu options
    print("""
            • 1. Register student
            • 2. Consult student
            • 3. Update grades
            • 4. Delete student
            • 5. View all students
            • 6. Exit
        """)

    option = input("Please enter an option: ")

    match option:
        case "1":
            # Register a new student
            name = input("Enter the name: ")
            name = validate_name_input(name)
            
            id_number = input("Enter the ID number: ")
            id_number = validate_number_input(id_number)
            
            age = input("Enter the age: ")
            age = validate_number_input(age)
            
            grades_input = input("Enter at least 3 grades separated by ',': ")
            grades = grades_input.split(",")
            
            stored_grades = []
            for grade in grades:
                if grade.isalpha():  # Check if the grade is a non-numeric value
                    print("Only numbers will be considered.")
                else:
                    grade = float(grade)
                    if 0 <= grade <= 100:  # Check if the grade is within the valid range
                        stored_grades.append(grade)
                    else:
                        print("The grade must be a positive number less than or equal to 100.")

            student = { 
                "name": name,
                "id": id_number,
                "age": age,
                "grades": stored_grades
            }
            students.append(student)
            print("Data saved successfully.")
        
        case "2":
            # Consult a student by their ID
            search_id = input("Enter the ID number of the student to consult: ")
            found = None
            for student in students:
                if student["id"] == search_id:
                    found = student
                    break
                
            if found is None:
                print("🔍 Student not found.")
            else:
                grades = found["grades"]
                average = sum(grades) / len(grades) if grades else 0
                print(f"Name: {found['name']}")
                print(f"Age: {found['age']}")
                print(f"Grades: {grades}")
                print(f"Average: {average:.2f}")
        
        case "3":
            # Update grades of a student
            search_id = input("Enter the ID number of the student to update grades: ")
            found = None
            for student in students:
                if student["id"] == search_id:
                    found = student
                    break

            if not found:
                print("🔍 Student not found.")
            else:
                print(f"Current grades: {found['grades']}")
                new_grades = input("Enter new grades separated by ',': ").split(",")
                stored_grades = []
                for grade in new_grades:
                    if grade.strip().replace('.','',1).isdigit():  # Check if the input is a number
                        grade = float(grade)
                        if 0 <= grade <= 100:  # Check if the grade is within the valid range
                            stored_grades.append(grade)
                        else:
                            print(f"Grade {grade} ignored: out of range.")
                    else:
                        print(f"Input {grade} ignored: not a number.")
                if stored_grades:
                    found["grades"] = stored_grades  # Update the student's grades
                    print("Grades updated:", found["grades"])
                else:
                    print(" No grades updated: empty or invalid input.")

        case "4":
            # Delete a student by their ID
            search_id = input("Enter the ID number of the student to delete: ")
            before = len(students)
            students[:] = [s for s in students if s["id"] != search_id]  # Filter the list of students
            if len(students) < before:
                print(" Student deleted.")
            else:
                print("🔍 Student not found.")

        case "5":
            # View all registered students
            if students:
                print(" List of students:")
                for s in students:
                    print(f"- ID {s['id']}: {s['name']} (age {s['age']})")
            else:
                print(" No students registered yet.")

        case "6":
            # Exit the program
            print(" Exiting the system...")

        case _:
            # Handle invalid options
            print("Invalid option. Please enter a number between 1 and 6.")

