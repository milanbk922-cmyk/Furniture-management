import calendar
from decimal import Decimal, ROUND_HALF_UP

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone
from .models import Attendance, EmployeeMoneyTaken, MonthlySalary

@transaction.atomic
def calculate_employee_salary(employee, month, year):
    # Validate the selected month
    if month < 1 or month > 12:
        raise ValidationError("Month must be between 1 and 12.")

    if year <  2000 or year > timezone.localdate().year + 1:
        raise ValidationError("Invalid salary year.")

    #Find the first and last day of the selected month
    last_day = calendar.monthrange(year, month)[1]
    start_date = timezone.datetime(year, month, 1).date()
    end_date= timezone.datetime(year, month, last_day).date()

    #Get attendace records for this employee and month
    attendance_records = Attendance.objects.filter(
        emplyee= employee,
        date_range= (start_date, end_date)
    )
    attendance_data = attendance_records.aggregate(
        total_hours = Sum("status")
    )
    total_hours = attendance_data["total_hours"] or 0
    recorded_days = attendance_records.count()

    # Calculate salary using daily salary / 10 hours
    daily_salary = employee.salary
    hourly_rate = daily_salary / Decimal("10")
    gross_salary = (
        hourly_rate * Decimal(total_hours)
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Calculate advances taken during this month
    advance_amount = EmployeeMoneyTaken.objects.filter(
        employee=employee,
        date__range=(start_date, end_date)
    ).aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")
    advance_amount = advance_amount.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
    payable_amount = (
        gross_salary - advance_amount
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    #Find or create the monthly salary record
    salary_record, created = MonthlySalary.objects.get_or_create(
        employee=employee,
        month=month,
        year=year,
        defaults={
            "daily_salary": daily_salary,
            "recorded_days": recorded_days,
            "total_hours": total_hours,
            "gross_salary": gross_salary,
            "advance_amount": advance_amount,
            "payable_amount": payable_amount,
        }
    )

    #Never overwrite an already-paid salary
    if not created and salary_record.payment_status == "paid":
        raise ValidationError(
            "This salary has already been paid and cannot be recalculated."
        )
    if not created:
        salary_record.daily_salary = daily_salary
        salary_record.recorded_days = recorded_days
        salary_record.total_hours = total_hours
        salary_record.gross_salary = gross_salary
        salary_record.advance_amount = advance_amount
        salary_record.payable_amount = payable_amount
        salary_record.save()

    return salary_record