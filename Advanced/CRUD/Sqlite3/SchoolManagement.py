import sqlite3

class SchoolManagement:
    def __init__(self,db_name = 'SchoolManagement.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute('pragma foreign_key=on')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
                            create table if not exists Students(
                                id integer primary key autoincrement,
                                name text not null,
                                family text not null
                            )
                            ''')
    def create_tables(self):
        self.cursor.execute('''
                            create table if not exists Teachers(
                                id integer primary key autoincrement,
                                name text not null,
                                family text not null
                            )
                            ''')
        self.cursor.execute('''
                            create table if not exists Course(
                                id integer primary key autoincrement,
                                name text not null
                            )
                            ''')
        self.cursor.execute('''
                            create table if not exists Teacher_course(
                            id integer primary key autoincrement,
                            teacher_id integer not null,
                            course_id integer not null,
                            foreign key (teacher_id) references teacher(id) on delete cascade,
                            foreign key (course_id) references course(id) on delete cascade,
                            unique (teacher_id, course_id)
                            )
                            ''')
        self.cursor.execute('''
                            create table if not exists Grades(
                            id integer primary key autoincrement,
                            student_id integer not null,
                            course_id integer not null'
                            score real not null,
                            foreign key (student_id) references student(id) on delete cascade,
                            foreign key (c
                            ourse_id) references course(id) on delete cascade
                            )
                            ''')
#..............................................................................................................................
    def add_student(self,name,family):
        sql = 'insert into Students (name,family) values (?,?)'
        val = (name,family)
        self.cursor.execute(sql,val)
        self.conn.commit()

    def add_teacher(self,name,family):
        sql = 'insert into Teachers (name,family) values (?,?)'
        val = (name,family)
        self.cursor.execute(sql,val)
        self.conn.commit()

    def add_course(self,name):
        sql = 'insert into Course (name) values (?)'
        val = (name,)
        self.cursor.execute(sql,val)
        self.conn.commit()

    def add_grade(self,student_id,course_id,score):
        if self.check_student_exists(student_id) is None or self.check_course_exists(course_id) is None:
            print('Student id or course id not found!')
        else:
            sql = 'insert into Grades (student_id,course_id,score) values (?,?,?)'
            val = (student_id,course_id,score)
            self.cursor.execute(sql,val)
            self.conn.commit()

    def add_teacher_course(self,teacher_id,course_id):
        if self.check_teacher_exists(teacher_id) is None or self.check_course_exists(course_id) is None:
            print('Teacher id or course id not found!')
        else:
            try:
                sql = 'insert into teacher_course(teacherid,teacher_course) values (?,?)'
                val = (teacher_id,course_id)
                self.cursor.execute(sql,val)
                self.conn.commit()
            except sqlite3.Error as er:
                print(er)
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

    def check_grade_exists(self,student_id):
        sql = 'select * from Grade where id=?'
        val = (student_id)
        return self.cursor.execute(sql,val).fetchone()
    
    def check_teacher_course_exists(self,teacher_id):
        sql = 'select * from Teacher_course where id=?'
        val = (teacher_id)
        return self.cursor.execute(sql,val).fetchone()
#..............................................................................................................................
    def show_students(self):
        students = self.cursor.execute('select * from Students').fetchall()
        return students

    def show_teachers(self):
        teachers = self.cursor.execute('select * from Teachers').fetchall()
        return teachers

    def show_courses(self):
        courses = self.cursor.execute('select * from Course').fetchall()
        return courses

    def show_grades(self):
        grades = self.cursor.execute('select * from Grades').fetchall()
        return grades

    def show_teacher_course(self):
        teachers = self.cursor.execute('select * from Teacher_course').fetchall()
        return teachers
#..............................................................................................................................
    def delete_student(self,student_id):
        if self.check_student_exists(student_id):
            #if self.check_grade_exists(student_id):
            #   sql = 'delete from Grades where student_id:?'
            #   val = (student_id)
            #   self.cursor.execute(sql,val)
            #   self.conn.commit()
               sql = 'delete from Students where student_id:?'
               val = (student_id)
               self.cursor.execute(sql,val)
               self.conn.commit()
        else:
            print('Student id not found!')

    def delete_teacher(self,teacher_id):
        if self.check_teacher_exists(teacher_id):
               sql = 'delete from Teachers where teacher_id:?'
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

    def delete_grade(self,grade_id):
        if self.check_grade_exists(grade_id):
               sql = 'delete from Grades where grade_id:?'
               val = (grade_id)
               self.cursor.execute(sql,val)
               self.conn.commit()
        else:
            print('Grade id not found!')

    def delete_teacher_course(self,teacher_id):
        if self.check_teacher_course_exists(teacher_id):
               sql = 'delete from teacher_courses where teacher_id:?'
               val = (teacher_id)
               self.cursor.execute(sql,val)
               self.conn.commit()
        else:
            print('teacher_course id not found!')
#..............................................................................................................................
    def update_student(self,student_id,new_name,new_family):
        if self.check_student_exists(student_id):
            self.cursor.execute('update Students set name=?, family=? where id=?', (new_name,new_family,student_id))
            self.conn.commit()
            print(f'Student with id {student_id} updated')

    def update_teacher(self,teacher_id,new_name,new_family):
        if self.check_teacher_exists(teacher_id):
            self.cursor.execute('update Teachers set name=?, family=? where id=?', (new_name,new_family,teacher_id))
            self.conn.commit()
            print(f'Teacher with id {teacher_id} updated')

    def update_course(self,course_id,new_name):
        if self.check_course_exists(course_id):
            self.cursor.execute('update Course set course=? where id=?', (new_name,course_id))
            self.conn.commit()
            print(f'course with id {course_id} updated')

    def update_grade(self,grade_id,new_student_id,new_course_id,new_score):
        if self.check_grade_exists(grade_id):
            self.cursor.execute('update Grades set score=?, student_id=?, course_id=? where id=?', (new_score,new_course_id,new_student_id,grade_id))
            self.conn.commit()
            print(f'Grade with id {grade_id} updated')

    def update_teacher_course(self,teacher_id,new_teacher_id,new_course_id):
        if self.check_teacher_course_exists(teacher_id):
            self.cursor.execute('update Teacher_course set teacher_id=?, course_id=? where id=?', (teacher_id,new_course_id,new_teacher_id))
            self.conn.commit()
            print(f'Teacher course with id {teacher_id} updated')