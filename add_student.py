import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'classroom.db')

def add_student(first_name, last_name, age, grade, seat_number):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (first_name, last_name, age, grade, seat_number)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, age, grade, seat_number))
    conn.commit()
    conn.close()
    print(f"Student {first_name} {last_name} added successfully!")

# Example: Add students
add_student("Fritz Vohn", "Dayday", 17, "12", 1)