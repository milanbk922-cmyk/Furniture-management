from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def employee(request):
    return render(request, "employees/employee.html")
def order(request):
    return render(request, "orders/order.html")
def employee_detail(request):
    return render(request, "employees/employee_detail.html")
def employee_form(request):
    return render(request, "employees/employee_form.html")
def order_detail(request):
    return render(request, "orders/order_detail.html")
def order_form(request):
    return render(request, "orders/order_form.html")
