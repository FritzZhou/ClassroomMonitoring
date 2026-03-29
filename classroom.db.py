import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'classroom.db')
print("Database will be created at:", db_path)

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
print("Database and students table created successfully!")