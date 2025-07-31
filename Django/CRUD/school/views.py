from django.shortcuts import render,redirect
from .models import Teacher,Student, Grade
from .forms import TeacherCreateForm, StudentCreateForm, GradeCreateForm, TeacherUpdateForm, StudentUpdateForm, GradeUpdateForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'school/index.html')
#........................................................................................
def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request,'school/list_teachers.html',{'teachers':teachers})

def list_students(request):
    students = Student.objects.all()
    return render(request,'school/list_students.html',{'students':students})

def list_grades(request):
    grades = Grade.objects.all()
    return render(request,'school/list_grades.html',{'grades':grades})
#........................................................................................
def teacher_details(request,id):
    teacher = Teacher.objects.get(id=id)
    return render(request,'school/teacher_details.html',{'teacher':teacher})

def student_details(request,id):
    student = Student.objects.get(id=id)
    return render(request,'school/student_details.html',{'student':student})

def grade_details(request,id):
    grade = Grade.objects.get(id=id)
    return render(request,'school/grade_details.html',{'grade':grade})
#........................................................................................
def teacher_delete(request,id):
    Teacher.objects.get(id=id).delete()
    messages.success(request,'teacher deleted succesfully!',extra_tags='success')   
    return redirect('list_teachers')

def student_delete(request,id):
    Student.objects.get(id=id).delete()
    messages.success(request,'student deleted succesfully!',extra_tags='success')
    storage = messages.get_messages(request)
    storage.used = True    
    return redirect('list_students')

def grade_delete(request,id):
    Grade.objects.get(id=id).delete()
    messages.success(request,'grade deleted succesfully!',extra_tags='success')
    storage = messages.get_messages(request)
    storage.used = True    
    return redirect('list_grades')
#........................................................................................
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Teacher.objects.create(name=cd['name'],family=cd['family'],subject=cd['subject'])
        messages.success(request,'teacher created succesfully!',extra_tags='success')
        return render(request,'school/teacher_create.html',{'form':form})
    if request.method == 'GET':
        form = TeacherCreateForm()
        #messages.success(request,'record created succesfully!',extra_tags='success')       
        return render(request,'school/teacher_create.html',{'form':form})
    
    
def student_create(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Student.objects.create(name=cd['name'],family = cd['family'],teacher = cd['teacher'])
            messages.success(request,'student created succesfully!',extra_tags='success')
            return render(request,'school/student_create.html',{'form':form})
    if request.method == 'GET':
        form = StudentCreateForm()
        #messages.success(request,'record created succesfully!',extra_tags='success') 
        return render(request,'school/student_create.html',{'form':form})

def grade_create(request):
    if request.method == 'POST':
        form = GradeCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Grade.objects.create(subject=cd['subject'], grade = cd['grade'], student = cd['student'])
            messages.success(request,'grade created succesfully!',extra_tags='success')    
        storage = messages.get_messages(request)
        storage.used = True        
        return render(request,'school/grade_create.html',{'form':form})
    if request.method == 'GET':
        form = GradeCreateForm()
        #messages.success(request,'record created succesfully!',extra_tags='success')
        storage = messages.get_messages(request)
        storage.used = True        
        return render(request,'school/grade_create.html',{'form':form})
#........................................................................................
def teacher_update(request,id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherUpdateForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request,'teacher updated succesfully!',extra_tags='success')     
            return redirect('list_teachers')
    else:
        form = TeacherUpdateForm(instance=teacher)
        #messages.success(request,'record updated succesfully!',extra_tags='success')       
        return render(request,'school/teacher_update.html',{'form':form})
    
def student_update(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'student updated succesfully!',extra_tags='success')     
            return redirect('list_students')
    else:
        form = StudentUpdateForm(instance=student)
        #messages.success(request,'record updated succesfully!',extra_tags='success')     
        return render(request,'school/student_update.html',{'form':form})
    
def grade_update(request,id):
    grade = Grade.objects.get(id=id)
    if request.method == 'POST':
        form = GradeUpdateForm(request.POST,instance=grade)
        messages.success(request,'grade updated succesfully!',extra_tags='success')
        if form.is_valid():
            form.save()    
            return redirect('list_grades')
    else:
        form = GradeUpdateForm(instance=grade)
        #messages.success(request,'record updated succesfully!',extra_tags='success')   
        return render(request,'school/grade_update.html',{'form':form})