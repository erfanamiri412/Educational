from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=30)
    temperature = models.FloatField()
    humidity = models.FloatField()
    icon = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.city} is {self.temperature} °C'