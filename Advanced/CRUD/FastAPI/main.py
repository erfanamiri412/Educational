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


@app.put('/update/{id:int}')
def update_student(id: int, name: str, family: str):
    student = Student.get(id=id)
    student.name = name
    student.family = family
    student.save()
    return {'name': name, 'family': family}


@app.delete('/delete/{id:int}')
def delete_student(id: int):
    student = Student.get(id=id)
    student.delete_instance()
    return {'id': id}