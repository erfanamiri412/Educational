import mysql.connector # type: ignore

class SchoolManagement():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.create_database()
        self.create_tables()

    def create_database(self):
        self.connection = mysql.connector.connect(
        host = self.host,
        user = self.user,
        password = self.password
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(f'create database if not exists {self.database}')
        self.connection.database = self.database

    def create_tables(self):
        self.cursor.execute("""
                            create table if not exists Student(
                                id int auto_increment primary key,
                                name varchar(50) not null,
                                family varchar(50) not null,
                                email varchar(50) unique
                            )
                            """)
        self.cursor.execute("""
                            create table if not exists Teacher(
                                id int auto_increment primary key,
                                name varchar(50) not null,
                                family varchar(50) not null,
                                email varchar(50) not null
                            )
                            """)
        self.cursor.execute("""
                            create table if not exists Course(
                                id int auto_increment primary key,
                                course varchar(50) not null    
                            )
                            """)
#..............................................................................................................................
    def add_student(self,name,family,email):
        sql = 'insert into Students (name,family,email) values (?,?,?)'
        val = (name,family,email)
        self.cursor.execute(sql,val)
        self.conn.commit()

    def add_teacher(self,name,family,email):
        sql = 'insert into Teachers (name,family,email) values (?,?,?)'
        val = (name,family,email)
        self.cursor.execute(sql,val)
        self.conn.commit()

    def add_course(self,name):
        sql = 'insert into Course (name) values (?)'
        val = (name,)
        self.cursor.execute(sql,val)
        self.conn.commit()
#..............................................................................................................................
    def check_student_exists(self,student_id):
        sql = 'select * from Students where id=?'
        val = (student_id)
        return self.cursor.execute(sql,val).fetchone()
    
    def check_teacher_exists(self,teacher_id):
        sql = 'select * from Teachers where id=?'
        val = (teacher_id)
        return self.cursor.execute(sql,val).fetchone()

    def check_course_exists(self,course_id):
        sql = 'select * from Course where id=?'
        val = (course_id)
        return self.cursor.execute(sql,val).fetchone()
#..............................................................................................................................
    def show_students(self):
        students = self.cursor.execute('select * from Student').fetchall()
        return students

    def show_teachers(self):
        teachers = self.cursor.execute('select * from Teacher').fetchall()
        return teachers

    def show_courses(self):
        courses = self.cursor.execute('select * from Course').fetchall()
        return courses
#..............................................................................................................................
    def delete_student(self,student_id):
        if self.check_student_exists(student_id):
               sql = 'delete from Student where student_id:?'
               val = (student_id)
               self.cursor.execute(sql,val)
               self.conn.commit()
        else:
            print('Student id not found!')

    def delete_teacher(self,teacher_id):
        if self.check_teacher_exists(teacher_id):
               sql = 'delete from Teacher where teacher_id:?'
               val = (teacher_id)
               self.cursor.execute(sql,val)
               self.conn.commit()
        else:
            print('Teacher id not found!')


    def delete_course(self,course_id):
        if self.check_course_exists(course_id):
               sql = 'delete from Course where course_id:?'
               val = (course_id)
               self.cursor.execute(sql,val)
               self.conn.commit()
        else:
            print('Course id not found!')
#..............................................................................................................................
    def update_student(self,student_id,new_name,new_family,new_email):
        if self.check_student_exists(student_id):
            self.cursor.execute('update Students set name=?, family=?, email=? where id=?', (new_name,new_family,new_email,student_id))
            self.conn.commit()
            print(f'Student with id {student_id} updated')

    def update_teacher(self,teacher_id,new_name,new_family,new_email):
        if self.check_teacher_exists(teacher_id):
            self.cursor.execute('update Teachers set name=?, family=?, email=? where id=?', (new_name,new_family,new_email,teacher_id))
            self.conn.commit()
            print(f'Teacher with id {teacher_id} updated')

    def update_course(self,course_id,new_course):
        if self.check_course_exists(course_id):
            self.cursor.execute('update Course set course=? where id=?', (new_course,course_id))
            self.conn.commit()
            print(f'course with id {course_id} updated')