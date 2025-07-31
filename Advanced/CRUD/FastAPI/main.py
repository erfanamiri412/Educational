from fastapi import FastAPI
from models import Student

app = FastAPI()


@app.get('/students')
def show_students():
    students = Student.select()
    return [{'name': student.name, 'family': student.family} for student in students]


@app.post('/add')
def add_student(name: str, family: str):
    # student = Student(name=name, family=family)
    # student.save()
    Student.create(name=name, family=family)
    return {'name': name, 'family': family}
