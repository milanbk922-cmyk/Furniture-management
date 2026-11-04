from django.db import models
from employees.models import Employee
# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present','Present'),
        ('Absent','Absent'),
        ('Hours','Hours'),
    ]
    employee = models.ForeignKey(
        Employee, 
        on_delete = models.CASCADE
    )
    date = models.DateField()
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Present'
    )

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.name}-{self.date}"

class EmployeeMoneyTaken(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='money_transactions'
    )
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    reason = models.CharField(
        max_length = 250,
        blank = True
    )
    def __str__(self):
        return f"{self.employee.name} - Rs. {self.amount} - {self.date}"