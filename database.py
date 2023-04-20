import sqlite3
from sqlite3 import Error #just in case  something goes wrong

def create_connection(db_file):
    c = None
    try:
        c = sqlite3.connect(db_file)
        return c
    except Error as e:
        print(e)

    return c

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_question(conn, para):
    test = test

def main():
    db = "database.db"
    create_classroom_table = """
CREATE TABLE IF NOT EXISTS classroom (
    classid integer PRIMARY KEY,
    classname text,
    teacherid integer,
    questionscorrectclass integer,
    questionsattemptedclass integer);"""
    create_student_table = """
CREATE TABLE IF NOT EXISTS students (
    studentid integer PRIMARY KEY,
    studentname text,
    password text,
    classid integer,
    questionsattempted integer,
    questionscorrect integer);"""
    create_teacher_table = """
CREATE TABLE IF NOT EXISTS teachers (
    teacherid integer PRIMARY KEY,
    teachername text,
    password text,
    classid integer);"""
    create_quiz_table = """
CREATE TABLE IF NOT EXISTS quiz (
    qnum integer PRIMARY KEY,
    qtext text,
    answer text,
    fakeanswer text,
    fakeranswer text);"""
    create_plane_table = """
CREATE TABLE IF NOT EXISTS 'planes' (
    planeid integer PRIMARY KEY,
    planename text,
    velocity float,
    wingarea float);"""
    conn = create_connection(db)
    print(conn)
    if conn is not None:
        create_table(conn, create_student_table)
        create_table(conn, create_classroom_table)
        create_table(conn, create_teacher_table)
        create_table(conn, create_quiz_table)
        create_table(conn, create_plane_table)

        
main()
print("done")
