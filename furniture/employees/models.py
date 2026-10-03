from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length = 100)
    Phone = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 100)
    Salary = models.DecimalField(max_digits = 10, decimal_places = 2)
    Joining_date = models.DateField()
    is_active = models.BooleanField(default = True)
    def __str__(self):
        return self.Name