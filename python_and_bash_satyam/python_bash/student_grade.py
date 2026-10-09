# student names as keys and grades as values
Student = {} #dictionary


#running until the user chooses "exit"
while True:

    # Ask the user which operation they want to perform
    action = input(
        "\nEnter operation [add, update, view, exit]: "
    ).strip().lower()


    # ADD A NEW STUDENT
    if action == "add":

        # Asking  student's name
        key = input("Enter student's name: ").strip()

        # Check if the student already exists
        if key in Student:
            print(f"Student '{key}' already exists.")

        # If student doesn't exist, add them to dictionary
        else:
            # Ask for the student's grade
            value = input(f"Enter grade for '{key}': ").strip()

            # Add name as key and grade as value
            Student[key] = value

            print(f"Student '{key}' added successfully.")


    # --------------------------------------------------
    # UPDATE AN EXISTING STUDENT'S GRADE
    # --------------------------------------------------
    elif action == "update":

        # Ask which student's grade should be updated
        key = input("Enter student's name: ").strip()

        # Check if the student exists
        if key in Student:

            # Ask for the new grade
            value = input(
                f"Enter new grade for '{key}': "
            ).strip()

            # Update the student's existing grade
            Student[key] = value

            print(f"Grade updated for '{key}'.")

        # Student does not exist
        else:
            print(f"Student '{key}' does not exist.")


    # VIEW ALL STUDENTS
    elif action == "view":

        # Check whether the dictionary contains any students
        if Student:

            print("\nStudent Grades:")

            # Loop through every key/value pair
            # student = key
            # grade = value
            for student, grade in Student.items():

                # Display student name and grade
                print(f"{student}: {grade}")

        # Dictionary is empty
        else:
            print("No students found.")


    # EXIT THE PROGRAM
    elif action == "exit":

        # Display exit message
        print("Exiting program...")

        # Stop the while loop
        break


    # INVALID OPERATION
    else:

        # Runs when the user enters something other
        # than add, update, view, or exit
        print(
            "Invalid operation. "
            "Please choose add, update, view, or exit."
        )