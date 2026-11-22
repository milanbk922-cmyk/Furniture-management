from django.db import models
from django.db.models import Q
from django.utils import timezone
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

class MonthlySalary(models.Model):
    PAYMENT_STATUS = [
        ("pending", "Pending"),
        ("paid", "Paid"),
    ]

    employee = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT,
        related_name="monthly_salaries"
    )
    month = models.PositiveSmallIntegerField()
    year= models.PositiveBigIntegerField()

    # snapshot of employee's daily salary
    daily_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    recorded_days = models.PositiveSmallIntegerField(default=0)
    total_hours = models.PositiveSmallIntegerField(default=0)

    #Salary earned before deducting advances
    gross_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    advance_amount = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    payable_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS,
        default="pending"
    )
    calculated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-year", "-month"]
        constraints=[
            models.UniqueConstraint(
                fields=["employee", "month", "year"],
                name= "unique_employee_monthly_salary"
            ),
            models.CheckConstraint(
                condition=Q(month__gte=1, month__lte=12),
                name="valid_monthly_salary_month"
            ),
        ]
    def __str__(self):
        return f"{self.employee.name}-{self.month}/{self.year}"