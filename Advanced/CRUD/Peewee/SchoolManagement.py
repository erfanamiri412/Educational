from peewee import SqliteDatabase, Model, TextField, IntegerField, ForeignKeyField, DecimalField
# ORM = Object Relational Mapping

db = SqliteDatabase('SchoolManagement.db')

class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    name = TextField()
    family = TextField()
    age = IntegerField()

class Teacher(BaseModel):
    name = TextField()
    family = TextField()
    subject = TextField()

class Grade(BaseModel):
    student = ForeignKeyField(Student, backref = 'grades')
    teacher = ForeignKeyField(Teacher, backref = 'grades')
    score = DecimalField()

db.create_tables([Student, Teacher, Grade])

# *insert into*:
# 1) st1 = Student(name = 'ali', family = ' mohammadi', age = 20)
#    st1.save()
# 2) Student.create(name = 'ali', family = ' mohammadi', age = 20)
# 3) st = Student.insert(name = 'ali', family = ' mohammadi', age = 20)
#    st.execute()
#    print(st.sql())

# *Select*:
# 1) students = Student.select()
#    for student in students:
#        print(f'{student.name}, {student.family}, {student.age}')

# *Delete*:
# 1) s = Student.get(Student.id == 1)
#    s.delete_instance()
# 2) s = Student.delete().where(Student.id == 1)
#    s.execute()

# *Update*:
# 1) row = Student.get(Student.id == 1)
#    row.name = 'Mohammad'
#    row.family = 'Rahbary'
#    row.age = 28
#    row.save()
# 2) st = Student.update({Student.name:'Mohammad', Student.family:'Rahbary', Student.age:28}).where(Student.id == 1)
#    print(st.sql())