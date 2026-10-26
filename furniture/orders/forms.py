from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=[
            'customer_name',
            'customer_phone',
            'customer_address',
            'order_name',
            'quantity',
            'unit_price',
            'discount',
            'expected_delivery',
            'status',
            'assigned_employee',
            'notes',
        ]
        widgets={
            'order_date':forms.DateInput(
                attrs={'type':'date'}
            ),
            'expected_delivery':forms.DateInput(
                attrs={'type':'date'}
            ),
        }