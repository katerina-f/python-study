import psycopg2
from datetime import datetime, timedelta

conn = psycopg2.connect("dbname=netology_db user=netology_user")
cur = conn.cursor()

def main():
    drop = """
    """

    conn = psycopg2.connect("dbname=netology_db user=netology_user")
    cur = conn.cursor()
    cur.execute(""" DROP TABLE IF EXISTS students CASCADE;
                DROP TABLE IF EXISTS courses CASCADE;""")
    conn.commit()
    create_db()
    now = datetime.now()

    students_1 = [
    {'name': 'Kate', 'gpa': 15, 'birth': now - timedelta(365*20)},
    {'name': 'Maxim', 'gpa': 20, 'birth': now - timedelta(360*28)},
    {'name': 'Lena', 'gpa': 18, 'birth': now - timedelta(368*29)}
    ]
    students_2 = [
    {'name': 'Mike', 'gpa': 26, 'birth': now - timedelta(368*23)},
    {'name': 'Evan', 'gpa': 17, 'birth': now - timedelta(368*18)},
    {'name': 'Lucy', 'gpa': 16, 'birth': now - timedelta(368*25)},
    ]
    students_3 = [
    {'name': 'Ilona', 'gpa': 15.5, 'birth': now - timedelta(368*31)},
    {'name': 'Youra', 'gpa': 19, 'birth': now - timedelta(368*21)},
    {'name': 'Kostya', 'gpa': 21.7, 'birth': now - timedelta(368*19)},    ]
    courses = ['Proggraming on Python', 'Django']

    for course in courses:
        add_course(course)
    for student in students_1:
        add_student(student)

    add_students(1, students_2)
    add_students(2, students_3)

    print(get_student(3))
    print(get_students(2))
    cur.close()
    conn.close()

def create_db(): # создает таблицы
    tables = """CREATE TABLE courses (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL);
            CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            course_id INTEGER REFERENCES courses(id),
            name VARCHAR(100) NOT NULL,
            gpa numeric(10,2),
            birth timestamptz);"""

    cur.execute(tables)
    conn.commit()

def add_course(course):
    request = """
    insert into courses (name)
    values (%s)"""
    cur.execute(request, [course])
    conn.commit()


def get_students(course_id): # возвращает студентов определенного курса
    cur.execute('select * from students where course_id=%s', [course_id])
    return cur.fetchall()


def add_students(course_id, students): # создает студентов и
    for student in students:            # записывает их на курс
        name, gpa, birth = student.values()
        request = """
        insert into students (course_id, name, gpa, birth)
        values (%s, %s, %s, %s)"""
        cur.execute(request, (course_id, name, gpa, birth))
        conn.commit()


def add_student(student): # просто создает студента
    name, gpa, birth = student.values()
    request = """
    insert into students (name, gpa, birth)
    values (%s, %s, %s)"""
    cur.execute(request, (name, gpa, birth))
    conn.commit()


def get_student(student_id):
    cur.execute('select * from students where id=%s', [student_id])
    return cur.fetchall()


if __name__ == '__main__':
    main()
