from django.db import models
from employees.models import Employee
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending","Pending"),
        ("in progress","In Progress"),
        ("completed","Completed"),
        ("cancelled","Cancelled"),
    ]
    # customer information
    customer_name = models.CharField(max_length = 100)
    customer_phone = models.CharField(max_length = 10)
    customer_address = models.CharField(max_length=100)
    # order information
    order_name = models.CharField(max_length = 250)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )
    discount = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 0
    )
    order_date = models.DateTimeField(auto_now_add = True)
    expected_delivery = models.DateField(
        null = True,
        blank = True
       )
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default= "pending"
    )
    #Employee assigned
    assigned_employee = models.ForeignKey(
        Employee,
        on_delete = models.SET_NULL,
        null =True,
        blank = True,
        related_name = 'orders'
    )
    notes = models.TextField(blank = True)
    @property
    def total_price(self):
        return (self.quantity * self.unit_price) - self.discount
    
    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"
    class Meta:
        ordering = ["-order_date"]