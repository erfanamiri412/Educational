from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)  # real price
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)  # off price
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/product')
    is_sale = models.BooleanField(default=False)
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    SIZA_HA = (
        ('m', '32'),
        ('l', '47'),
        ('xl', '52'),
    )
    size = models.CharField(max_length=4, choices=SIZA_HA, default='32')

    def __str__(self): 
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) 
    address = models.CharField(default='', blank=True, null=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)