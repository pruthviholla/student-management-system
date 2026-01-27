
import sqlite3

# connect to database (it creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

def add_student():
  name = input("Enter name: ")
  age = int(input("Enter age: "))
  course = input("Enter course: ")

  cursor.execute("INSERT INTO students (name, age, course) VALUES(?,?,?)",(name, age, course))
  conn.commit()
  print("Student added successfully")

add_student()
