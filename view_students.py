import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'classroom.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()

print("\nAll Students in the Classroom:")
print("-"*50)
for student in all_students:
    print(f"ID: {student[0]}, Name: {student[1]} {student[2]}, Age: {student[3]}, Grade: {student[4]}, Seat: {student[5]}, Attendance: {student[6]}")

conn.close()