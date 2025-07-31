from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField()
    family = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.family}"
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.family}"
    
class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.CharField()
    grade = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f'{self.grade}'