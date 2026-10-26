from django.urls import path
from . import views
urlpatterns=[
    path('list/', views.order_list, name='order_list'),
    path('add/', views.order_create, name='order_create'),
    path('<int:pk>', views.order_detail, name='order_detail'),
    path('edit/<int:pk>', views.order_edit,name='order_edit'),
    
]