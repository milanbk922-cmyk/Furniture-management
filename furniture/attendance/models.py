from django.db import models
from employees.models import Employee
# Create your models here.
class Attendance(models.Model):

    class AttendanceStatus(models.IntegerChoices):
        ABSENT = 0, 'Absent'
        ONE_HOUR = 1, '1 Hour'
        TWO_HOURS = 2, '2 Hours'
        THREE_HOURS = 3, '3 Hours'
        FOUR_HOURS = 4, '4 Hours'
        FIVE_HOURS = 5, '5 Hours'
        SIX_HOURS = 6, '6 Hours'
        SEVEN_HOURS = 7, '7 Hours'
        EIGHT_HOURS = 8, '8 Hours'
        NINE_HOURS = 9, '9 Hours'
        PRESENT = 10, 'Present'

    employee = models.ForeignKey(
        Employee, 
        on_delete = models.CASCADE
    )
    date = models.DateField()
    status = models.IntegerField(
        choices = AttendanceStatus.choices,
        default = 10
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
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.employee.name} - Rs. {self.amount} - {self.date}"