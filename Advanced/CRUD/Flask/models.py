from peewee import SqliteDatabase, Model, TextField

db = SqliteDatabase('Flask-CRUD.db')

class Student(Model):
    name = TextField()
    family = TextField()

    class Meta:
        database = db
        db_table = 'Student'

Student.create_table()