from django.urls import path
from . import views
urlpatterns = [
    path('attendance/', views.attendance, name="attendance"),
    path('attendance/detail/<int:pk>', views.attendance_detail, name="attendance_detail"),
    path('attendance/save/', views.save_attendance, name='save_attendance'),
    path('monthly_salaries/', views.monthly_salary_list, name="monthly_salary_list"),
    
]