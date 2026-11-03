from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.db import transaction
from .models import Employee, Attendance
from django.views.decorators.http import require_POST
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
    employee_data = [
        {
            'employee':employee,
            'status':attendance_map.get(
                employee.id,"Not Marked"
            )
        }
        for employee in employees
    ]
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
def attendance_detail(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    return render(request, 'attendances/attendance_detail.html',{'employee':employee})
def monthly_salary_list(request):
    return render(request, 'attendances/monthlysalary.html')