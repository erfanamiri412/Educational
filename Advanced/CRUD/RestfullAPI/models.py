from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, IntegerField

db = SqliteDatabase('RestfullAPI-CRUD')


class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField(max_length=20)
    age = IntegerField()


class Teacher(BaseModel):
    name = CharField()
    subject = CharField()


class Grade(BaseModel):
    student = ForeignKeyField(Student, backref='grades', on_delete='CASCADE')
    teachers = ForeignKeyField(Teacher, backref='grades', on_delete='CASCADE')
    grade = IntegerField()


db.connect()
db.create_tables([Student, Teacher, Grade])
