"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 13
Topic: 2
Assignment: Simple Query
Date: 04/11/2023
"""
import sqlite3
from sqlite3 import Error

def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        print("sqlite3 version: " + sqlite3.version)
        return conn
    except Error as err:
        print(err)
    return None

def create_person(database, person):
    conn = create_connection(database)
    sql = '''INSERT INTO person(firstname,lastname) VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, person)
    conn.commit()
    return cur.lastrowid

def create_student(database, student):
    conn = create_connection(database)
    sql = '''INSERT INTO student(id, major, begin_date) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,student)
    conn.commit()
    return cur.lastrowid
    
def create_table(database, sql_create_table):
    conn = create_connection(database)
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def create_tables(database):
    sql_create_person_table = """CREATE TABLE IF NOT EXISTS person (
                id integer PRIMARY KEY,
                firstname text NON NULL,
                lastname text NON NULL
            );"""
    
    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                id integer PRIMARY KEY,
                major text,
                begin_date NON NULL
    );"""

    create_table(database, sql_create_person_table)
    create_table(database, sql_create_student_table)

def drop_tables(database):
    conn = create_connection(database)
    if conn is None:
        raise(ConnectionError)
    else:
        cur = conn.cursor()
        cur.execute('DROP TABLE person')
        cur.execute('DROP TABLE student')

def create_connection_and_tables(database):
    create_tables(database)

def select_all_persons(database):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute('SELECT * FROM person')
    rows = cur.fetchall()
    return rows

def select_all_students(database):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    database = 'pythonsqlite.db'

    #conn = create_connection(database)
    #with conn:
        #drop_tables(conn)
        #create_tables(conn)
        #person = ('Dominic','Wood')
        #person_id = create_person(conn,person)

        #student = (person_id, 'Software Design', '2020-01-01')
        #student_id = create_student(conn,student)

    rows = select_all_persons(database)
    for r in rows:
        print(r)

    rows = select_all_students(database)
    for r in rows:
        print(r)