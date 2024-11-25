# student_register.py
def reg_students():
    # Ask how many students are registering
    num_students = int(input("How many students are registering? "))

    # Open the file to write the student IDs
    with open("reg_form.txt", "w") as file:
        # For loop to register each student
        for i in range(num_students):
            # Ask for the student ID
            student_id = input(f"Enter the ID for student {i+1}: ")
            # Write the student ID to the file, followed by a dotted line
            file.write(f"Student ID: {student_id}\n")
            file.write("...............................................\n")

    print(f"Registration complete. {num_students} students have been registered.")

# Run the function
if __name__ == "__main__":
    reg_students()
