from peewee import SqliteDatabase, CharField, Model

db = SqliteDatabase('FastAPI-CRUD.db')


class Student(Model):  # ORM name
    name = CharField(max_length=20)
    family = CharField(max_length=20)

    class Meta:
        database = db
        db_table = 'Student'  # sqlite name


Student.create_table()
