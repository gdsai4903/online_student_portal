import sqlite3

con = sqlite3.connect('database/student.db')
cur = con.cursor()

cur.execute("SELECT course_name, course_fee FROM course")
for row in cur.fetchall():
    print(row[0], "-", row[1])