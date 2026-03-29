from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

db_path = os.path.join(os.getcwd(), 'classroom.db')

# Create table if it doesn't exist
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        grade = request.form['grade']
        seat = request.form['seat_number']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (first_name, last_name, age, grade, seat_number)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, int(age), grade, int(seat)))
        conn.commit()
        conn.close()
        return redirect('/view_students')
    return render_template('add_student.html')

@app.route('/view_students')
def view_students():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('view_students.html', students=students)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Render will set PORT
    app.run(host='0.0.0.0', port=port, debug=True)
