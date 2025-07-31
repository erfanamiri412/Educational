from django import forms
from .models import Teacher, Student, Grade

# class TeacherCreateForm(forms.Form):
#     name = forms.CharField()
#     family = forms.CharField()
#     subject = forms.CharField()

class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','family','subject']

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','family','teacher']

class GradeCreateForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject','grade','student']

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','family','subject']

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','family','teacher']

class GradeUpdateForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject','grade','student']