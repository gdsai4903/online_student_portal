import sqlite3

con = sqlite3.connect('database/student.db')
cur = con.cursor()

cur.execute("SELECT username FROM student")

# for user in cur.fetchall():
#     print(user)
    
print('bkaur456' in cur.fetchall()) 