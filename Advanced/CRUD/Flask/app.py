from flask import Flask, render_template, request, redirect, url_for, delete_instance
from models import Student

app = Flask(__name__)

@app.route('/index')
def index():
    students = Student.select().order_by(Student.id.desc())
    return render_template('students.html',students = students)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        f = request.form.get('fname')
        l = request.form['lname']
        Student.create(name = f, family = l)
        return redirect(url_for('index'))
    
    if request.method == 'GET':
        return render_template('create.html')
    
@app.route('/details/<int:id>')
def details(id):
    st = Student.get_by_id(id)
    return render_template('details.html', st = st)

@app.route('/delete/<int:id>')
def delete(id):
    st = Student.get_by_id(id)
    st = delete_instance()
    return redirect(url_for('index'))
    
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    st = Student.get_by_id(id)
    if request.method == 'POST':
        st.name = request.form['fname']
        st.family = request.form['lname']
        st.save()
        return redirect(url_for('index'))
    
    if request.method == 'GET':
        return render_template('update.html', st = st)

if __name__ == '__main__':
    app.run(debug = True)