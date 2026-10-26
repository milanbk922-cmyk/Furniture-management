from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import Order
from employees.models import Employee

# Create your views here.
def order_list(request):
    orders = Order.objects.all().order_by("-order_date")
    return render(request, "orders/order.html", {"orders":orders})

def order_create(request):
    form = OrderForm()
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
        else:
            print(form.errors)
    return render(request, "orders/order_form.html", {'form':form, 'employees':employees})

def order_detail(request, pk):
    order = get_object_or_404(Order,pk=pk)
    return render(request, "orders/order_detail.html",{'order':order})

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_edit.html' , {'form':form, 'order':order, 'employees':employees})