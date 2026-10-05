from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def employee(request):
    return render(request, "employees/employee.html")
def order(request):
    return render(request, "orders/order.html")