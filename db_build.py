import sqlite3
from functions import *


def create_database():
    """
    Create a new database
    """
    con = sqlite3.connect("database/student.db")
    con.close()

def create_student_table():
    con = sqlite3.connect("database/student.db")
    cur = con.cursor()
    # Drop the table if it exists
    db_drop_query = '''DROP TABLE IF EXISTS student'''
    
    # Create the table to hold the student data
    student_table_query = """CREATE TABLE IF NOT EXISTS student (
                              student_id    INTEGER PRIMARY KEY AUTOINCREMENT
                            , first_name    VARCHAR(35)  NOT NULL
                            , last_name     VARCHAR(35)
                            , dob           DATE
                            , email         VARCHAR(50)  UNIQUE
                            , username      VARCHAR(35)  UNIQUE
                            , password      CHAR(32)
                            , phone         CHAR(12)     UNIQUE
                            , addr          VARCHAR(60)
                            , status        CHAR(1)      NOT NULL DEFAULT 'U'
                            , active        BIT      NOT NULL DEFAULT  1)"""

    cur.execute(db_drop_query)
    cur.execute(student_table_query)
    
    con.commit()
    con.close()

def create_document_table():
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()
    
    
    db_drop_query = '''DROP TABLE IF EXISTS document'''
    document_table_query = """CREATE TABLE  IF NOT EXISTS document (
                                document_id INTEGER PRIMARY KEY AUTOINCREMENT
                              , student_id  INTEGER 
                              , doc_name    VARCHAR(100)
                              , active      BIT         NOT NULL DEFAULT 1
                              , CONSTRAINT  stu__FK     FOREIGN KEY (student_id) REFERENCES student)"""

    cur.execute(db_drop_query)
    cur.execute(document_table_query)
    
    con.commit()
    con.close()
    
def create_course_table():
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()
    
    db_drop_query = '''DROP TABLE IF EXISTS course'''
    course_table_query = """CREATE TABLE  IF NOT EXISTS course (
                                course_id    INTEGER PRIMARY KEY AUTOINCREMENT
                              , course_name  VARCHAR(35)   UNIQUE NOT NULL
                              , course_fee   NUMERIC(5,2)
                              , active       BIT           NOT NULL DEFAULT 1)"""

    populate_course_table = """INSERT INTO course (course_name, course_fee)
                                VALUES            ('Linear Algebra', 1700)
                                                , ('Statistics', 1650)
                                                , ('Programming', 1300)
                                                , ('Communications', 1100)
                                                , ('Intro to DSML', 1600)"""

    cur.execute(db_drop_query)
    cur.execute(course_table_query)
    set_initial_course_id(1001)
    cur.execute(populate_course_table)
    
    con.commit()
    con.close()
    
def create_amenity_table():
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()
    
    db_drop_query = '''DROP TABLE IF EXISTS amenity'''
    course_table_query = """CREATE TABLE  IF NOT EXISTS amenity (
                                amenity_id    INTEGER PRIMARY KEY AUTOINCREMENT
                              , amenity_name  VARCHAR(35)   UNIQUE NOT NULL
                              , amenity_fee   NUMERIC(5,2)
                              , active        BIT           NOT NULL DEFAULT 1)"""

    populate_course_table = """INSERT INTO amenity (amenity_name, amenity_fee)
                                VALUES             ('Association Fee', 150)
                                                 , ('Textbooks', 2000)
                                                 , ('Recreational Fee', 50)
                                                 , ('Building Fee', 20)"""

    cur.execute(db_drop_query)
    cur.execute(course_table_query)
    cur.execute(populate_course_table)
    
    con.commit()
    con.close()

def create_tax_table():
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()
    
    db_drop_query = '''DROP TABLE IF EXISTS tax'''
    tax_table_query = """CREATE TABLE IF NOT EXISTS taxes (
                          tax_id   INTEGER PRIMARY KEY AUTOINCREMENT
                        , tax_type CHAR(3)
                        , tax_beg  DATE
                        , tax_end  DATE
                        , tax_perc NUMERIC(4,2)
                        , active   BIT NOT NULL DEFAULT 1)"""
    
    populate_tax_table = """INSERT INTO taxes (tax_type, tax_beg, tax_end, tax_perc)  
                            VALUES            ('PST', '1987-07-01', '2013-06-30', 7.00)
                                            , ('GST', '1991-01-01', '1997-03-31', 7.00)
                                            , ('GST', '1997-04-01', '2007-12-31', 6.00)
                                            , ('GST', '2008-01-01', NULL, 5.00)
                                            , ('PST', '2013-07-01', '2018-06-30', 8.00)
                                            , ('PST', '2019-07-01', NULL, 7.00)"""
    cur.execute(db_drop_query)
    cur.execute(tax_table_query)
    cur.execute(populate_tax_table)
    
    con.commit()
    con.close()

def set_initial_course_id(start_id):
    """
    Set the initial student_id for the AUTOINCREMENT to start from a specific value
    """
    con = sqlite3.connect("database/student.db")
    cur = con.cursor()

    # Insert a dummy record to initialize sqlite_sequence if not already initialized
    cur.execute("INSERT INTO course (course_id, course_name) VALUES (?, 'dummy')", (start_id-1,))
    cur.execute("DELETE FROM course WHERE course_id = ?", (start_id-1,))

    con.commit()
    con.close()
       
def set_initial_student_id(start_id):
    """
    Set the initial student_id for the AUTOINCREMENT to start from a specific value
    """
    con = sqlite3.connect("database/student.db")
    cur = con.cursor()

    # Insert a dummy record to initialize sqlite_sequence if not already initialized
    cur.execute("INSERT INTO student (student_id, first_name) VALUES (?, 'dummy')", (start_id-1,))
    cur.execute("DELETE FROM student WHERE student_id = ?", (start_id-1,))

    con.commit()
    con.close()

def insert_student(f_name, l_name, dob, email, username, password, phone, addr):
    con = sqlite3.connect("database/student.db")
    cur = con.cursor()

    sample_data_query = f"""INSERT INTO student (first_name
                                                , last_name
                                                , dob
                                                , email
                                                , username
                                                , password
                                                , phone
                                                , addr)
                                        VALUES(?,?,DATE(?),?,?,?,?,?)"""
    cur.execute(sample_data_query, (f_name
                                , l_name
                                , dob
                                , email
                                , username
                                , MD5(password)
                                , phone
                                , addr))
    con.commit()
    con.close()


if __name__ == "__main__":
    create_database()
    create_student_table()
    create_document_table()
    create_course_table()
    create_amenity_table()
    create_tax_table()
    
    set_initial_student_id(100001)
    
    insert_student('Bavleen', 'Kaur', '2003-09-04', "gdsai4903@gmail.com", 'bkaur456', 'Password1', '123-456-7890', '315-19 St Michael Rd')
    insert_student('Gagandeep', 'Singh', '2001-09-24', "kaurbavleen2@gmail.com", 'gsingh123', 'Password2', '098-765-4321', '315-19 St Michael Rd')
    insert_student('Simranpreet', 'Singh', '2003-12-24', "ssimranpreet295@gmail.com", 'ssingh789', 'Password3', '098-123-4321', '123 Pembina Hwy')
    
    set_status('gsingh123', 'A')
