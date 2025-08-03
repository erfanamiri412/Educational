from flask import Flask, jsonify, request
from models import Student, Teacher, Grade

app = Flask(__name__)


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student.create(name=data['name'], age=data['age'])
    return jsonify({'id': student.id})


@app.route('/students', methods=['GET'])
def get_student():
    students = Student.select()
    return jsonify({'id': students.id, 'name': students.name, 'age': students.age} for student in students)


if __name__ == '__main__':
    app.run(debug=True)
