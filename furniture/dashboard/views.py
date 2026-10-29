from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
from orders.models import Order

# Create your views here.

def dashboard_view(request):
    orders=Order.objects.all()
    total_order_value = sum(
        order.total_price for order in orders
        )
    recent_orders = Order.objects.order_by("-order_date")[:5]

    context = {
        "total_employees" : Employee.objects.count(),
        "active_employees" : Employee.objects.filter(
            status=True
        ).count(),
        "total_orders" : Order.objects.count(),
        "pending_orders" : Order.objects.filter(
            status="pending"
        ).count(),
        "in_progress_orders" : Order.objects.filter(
            status="in progress"
        ).count(),
        "completed_orders" : Order.objects.filter(
            status="completed"
        ).count(),
        "total_order_value":int(total_order_value),
        "recent_orders": recent_orders,
    }
    return render(request, "home.html", context)

