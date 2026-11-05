from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.db import transaction
from django.views.decorators.http import require_POST
from decimal import Decimal, InvalidOperation

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
                    employee.id,"Not Marked"
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
            if status in ['Present','Absent','Hours']:
                Attendance.objects.update_or_create(
                    employee=employee,
                    date=selected_date,
                    defaults={'status':status}
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

def attendance_detail(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    return render(request, 'attendances/attendance_detail.html',{'employee':employee})
def monthly_salary_list(request):
    return render(request, 'attendances/monthlysalary.html')