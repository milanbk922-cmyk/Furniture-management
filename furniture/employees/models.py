from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    salary = models.DecimalField(max_digits = 10, decimal_places = 2)
    joining_date = models.DateField()
    status = models.BooleanField(default = True)
    def __str__(self):
        return self.name