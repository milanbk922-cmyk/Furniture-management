from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
from orders.models import Order

# Create your views here.
def attendance_list(request):
    return render(request, 'attendances/attendance.html')
def monthly_salary_list(request):
    return render(request, 'attendances/monthlysalary.html')