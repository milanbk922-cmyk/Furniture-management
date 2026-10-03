from django.db import models
from employees.models import Employee
# Create your models here.
class order(models.Model):
    Customer_name = models.CharField(max_length = 100)
    Contact = models.CharField(max_length = 10)
    Order_name = models.CharField(max_length = 250)
    Price = models.DecimalField(max_digits = 8 , decimal_places = 2)
    Employee = models.ForeignKey(
        Employee,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    def __str__(self):
        return self.Customer_name