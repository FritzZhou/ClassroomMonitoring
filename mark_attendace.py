import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'classroom.db')

def mark_attendance(student_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET attendance_count = attendance_count + 1
        WHERE student_id = ?
    ''', (student_id,))
    conn.commit()
    conn.close()
    print(f"Attendance marked for student ID {student_id}!")

# Example: Mark attendance for student ID 1 and 2
mark_attendance(1)
mark_attendance(2)