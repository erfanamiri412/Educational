from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('teachers/',views.list_teachers, name = 'list_teachers'),
    path('students/',views.list_students, name = 'list_students'),
    path('grades/',views.list_grades, name = 'list_grades'),
    path('teacher_details/<int:id>',views.teacher_details, name = "teacher_details"),
    path('student_details/<int:id>',views.student_details, name = "student_details"),
    path('grade_details/<int:id>',views.grade_details, name = "grade_details"),
    path('teacher_delete/<int:id>',views.teacher_delete, name = "teacher_delete"),
    path('student_delete/<int:id>',views.student_delete, name = "student_delete"),
    path('grade_delete/<int:id>',views.grade_delete, name = "grade_delete"),
    path('teacher_create/',views.teacher_create, name = 'teacher_create'),
    path('student_create/',views.student_create, name = 'student_create'),
    path('grade_create/',views.grade_create, name = 'grade_create'),
    path('teacher_update/<int:id>',views.teacher_update, name = 'teacher_update'),
    path('student_update/<int:id>',views.student_update, name = 'student_update'),
    path('grade_update/<int:id>',views.grade_update, name = 'grade_update'),
]
