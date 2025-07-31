from django.contrib import admin
from .models import Teacher,Student,Grade

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
# admin.site.register([Teacher,Student])