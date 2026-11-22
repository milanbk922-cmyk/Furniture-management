from django.contrib import admin
from .models import Attendance, EmployeeMoneyTaken, MonthlySalary
# Register your models here.
admin.site.register(Attendance)
admin.site.register(EmployeeMoneyTaken)
admin.site.register(MonthlySalary)