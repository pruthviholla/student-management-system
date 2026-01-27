import sqlite3

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")
conn.commit()

# Add student
def add_student():
    name = input("Enter name: ")
    course = input("Enter course: ")

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Age must be a number.")
        return

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("Student added successfully!")

# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\nID | Name | Age | Course")
    print("-" * 30)
    for s in students:
        print(s[0], s[1], s[2], s[3])

# Update student
def update_student():
    student_id = input("Enter student ID to update: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    course = input("Enter new course: ")

    try:
        age = int(input("Enter new age: "))
    except ValueError:
        print("Age must be a number.")
        return

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, student_id)
    )
    conn.commit()
    print("Student updated successfully!")

# Delete student
def delete_student():
    student_id = input("Enter student ID to delete: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student deleted successfully!")

# Main menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        conn.close()
        break
    else:
        print("Invalid choice. Try again.")
