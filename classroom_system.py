import sqlite3
import os

# Database setup
db_path = os.path.join(os.getcwd(), 'classroom.db')

def create_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        grade TEXT,
        seat_number INTEGER,
        attendance_count INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

# Add a student
def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    seat_number = int(input("Enter seat number: "))
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (first_name, last_name, age, grade, seat_number)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, age, grade, seat_number))
    conn.commit()
    conn.close()
    print(f"Student {first_name} {last_name} added successfully!\n")

# View all students
def view_students():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    
    if not students:
        print("No students found.\n")
        return
    
    print("\nAll Students:")
    print("-"*60)
    for s in students:
        print(f"ID: {s[0]}, Name: {s[1]} {s[2]}, Age: {s[3]}, Grade: {s[4]}, Seat: {s[5]}, Attendance: {s[6]}")
    print()

# Mark attendance
def mark_attendance():
    student_id = int(input("Enter student ID to mark attendance: "))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET attendance_count = attendance_count + 1
        WHERE student_id = ?
    ''', (student_id,))
    conn.commit()
    conn.close()
    print(f"Attendance marked for student ID {student_id}\n")

# Main menu
def main():
    create_database()
    while True:
        print("=== Classroom Monitoring System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()