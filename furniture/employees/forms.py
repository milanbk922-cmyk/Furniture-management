from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields=[
            'name',
            'phone',
            'address',
            'salary',
            'joining_date',
            'status',
        ]
        widgets={
            'joining_date':forms.DateInput(
                attrs={'type':'date'}
            ),
        }