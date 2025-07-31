from django.contrib import admin
from .models import Category, Customer, Product, Order

# Register your models here.

admin.site.register([Category, Customer, Product, Order])