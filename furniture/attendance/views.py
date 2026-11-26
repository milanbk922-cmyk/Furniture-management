from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import transaction
from django.views.decorators.http import require_POST
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from django.db.models import Count, Q, Sum

from employees.models import Employee
from .models import MonthlySalary
from .services import calculate_employee_salary

from .models import Employee, Attendance, EmployeeMoneyTaken
# Create your views here.
def attendance(request):
    selected_date = request.GET.get('date')
    if selected_date:
        selected_date = parse_date(selected_date)
    if not selected_date:
        from django.utils import timezone
        selected_date = timezone.localdate()
    employees = Employee.objects.filter(status=True)
    attendance_records = Attendance.objects.filter(
        date= selected_date
    )
    attendance_map = {
        record.employee_id : record.status
        for record in attendance_records
    }

    # Fetch money transactions for selected date
    money_records = EmployeeMoneyTaken.objects.filter(
        date=selected_date
    ).select_related('employee').order_by('created_at')

    money_map = {}

    for record in money_records:
        money_map.setdefault(record.employee_id, []).append(record)

    employee_data = []

    for employee in employees:
        transactions = money_map.get(employee.id, [])

        total_taken = sum(
            (item.amount for item in transactions),
            Decimal('0.00')
        )
        employee_data.append(
            {
                'employee':employee,
                'status':attendance_map.get(
                    employee.id, 10
                ),
                'money_transactions': transactions,
                'total_taken':total_taken,
            })
    
    return render(request, 'attendances/attendance.html',{
        'employee_data':employee_data,
        'selected_date':selected_date,
    })

@require_POST
def save_attendance(request):
    selected_date = parse_date(request.POST.get('date'))
    if not selected_date:
        return redirect(attendance)
    with transaction.atomic():
        for employee in Employee.objects.filter(status=True):
            status = request.POST.get(
                f'attendance_{employee.id}'
            )
            if status in [
                '0','1','2','3','4',
                '5','6','7','8','9','10'
                ]:
                Attendance.objects.update_or_create(
                    employee=employee,
                    date=selected_date,
                    defaults={'status':int(status)}
                )
    return redirect(f'/sidebar/attendance/?date={selected_date}')

@require_POST
def save_employee_money(request):
    selected_date = parse_date(request.POST.get('date', ''))
    employee_id = request.POST.get('employee_id')
    amount = request.POST.get('amount', '').strip()
    reason = request.POST.get('reason', '').strip()

    if not selected_date:
        return redirect(attendance)

    employee = get_object_or_404(
        Employee,
        id=employee_id,
        status=True
    )

    try:
        amount = Decimal(amount)
    except (InvalidOperation, TypeError):
        return redirect(f'/sidebar/attendance/?date={selected_date}')

    if amount <= 0:
        return redirect(f'/sidebar/attendance/?date={selected_date}')

    EmployeeMoneyTaken.objects.create(
        employee=employee,
        date=selected_date,
        amount=amount,
        reason=reason
    )

    return redirect(f'/sidebar/attendance/?date={selected_date}')

def monthly_salary_list(request):
    today = timezone.localdate()
    #Default to hte current month
    month = today.month
    year = today.year

    if request.method== "POST":
        month = int(request.POST.get("month", today.month))
        year = int(request.POST.get("year", today.year))
        employees = Employee.objects.filter(status=True)
        for employee in employees:
            try:
                calculate_employee_salary(employee, month, year)
            except ValidationError as error:
                messages.error(
                    request,
                    f"{employee.name}: {error}"
                )
        messages.success(
            request,
            "Monthly salary calculation have been processed."
        )

        return redirect(
            f"{request.path}?month={month}&year={year}" 
        )

    # Read selected month and year from the URL
    month = int(request.GET.get("month", month))
    year = int(request.GET.get("year", year))

    salary_records = MonthlySalary.objects.filter(
        month = month,
        year = year
    ).select_related("employee")

    context = {
        "active_employees" : Employee.objects.filter(
            status=True
        ).count(),
        "salary_records":salary_records,
        "month":month,
        "year":year,
        "employees":Employee.objects.filter(status=True)
    }
    return render(request, 'attendances/monthlysalary.html', context)

def salary_detail(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    today = timezone.localdate()
    try:
        month = int(request.GET.get("month",today.month))
        year = int(request.GET.get("year",today.year))
        date(year, month, 1)
    except(ValueError, TypeError):
        month = today.month
        year = today.year
    attendance_records = Attendance.objects.filter(
         employee=employee,
         date__year=year,
         date__month=month
     ).order_by("date")
    attendance_summary= attendance_records.aggregate(
        present=Count("id", filter=Q(status=10)),
        absent = Count("id", filter=Q(status=0)),
        partial=Count("id", filter=Q(status__gte=1, status__lte=9)),
    )
    advances = EmployeeMoneyTaken.objects.filter(
        employee=employee,
        date__year=year,
        date__month=month
    )
    # Total hours worked in the selected month
    total_hours = attendance_records.aggregate(
        total = Sum("status")
    )["total"] or 0

    #Employee's daily salary
    daily_salary = employee.salary
    # Calculate hourly rate
    hourly_rate = daily_salary / Decimal("10")
    # Calculate earned salary
    gross_salary=(
        hourly_rate * Decimal(total_hours)
    ).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
    # Calculate total advances
    advance_amount= advances.aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")
    # Calculate remaining payable salary
    payable_salary = (
        gross_salary - advance_amount
    ).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    context = {
        "employee": employee,
        "month":month,
        "year":year,
        "selected_date":date(year,month,1),
        "attendance_records":attendance_records,
        "advances":advances,
        "attendance_summary":attendance_summary,
        "daily_salary": daily_salary,
        "total_hours": total_hours,
        "hourly_rate": hourly_rate,
        "gross_salary": gross_salary,
        "advance_amount": advance_amount,
        "payable_salary": payable_salary,
    }
    return render(request, 'attendances/salary_detail.html',context)
