from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def employee_list(request):
    employees = Employee.objects.all().order_by("joining_date")
    return render(request, "employees/employee.html", {"employees":employees})

def employee_create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "employees/employee_form.html", {'form':form})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee,pk=pk)
    return render(request, "employees/employee_detail.html",{'employee':employee})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_detail", employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request,'employees/employee_edit.html' , {'form':form, 'employee':employee})
