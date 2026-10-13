from django.urls import path
from . import views
urlpatterns =[
    path('', views.home , name = 'home'),
    path('employee/', views.employee, name = 'employee'),
    path('employee/employee_form/', views.employee_form, name='employee_form'),
        
    path('order/', views.order, name='order'),
    path('order/order_form/', views.order_form, name='order_form'),
    path('order/order_detail/', views.order_detail, name='order_detail'),

]