from django.urls import path
from .views import EmployeeUpdateImage , EmployeeUpdate

urlpatterns = [    
    path('employeeupdate/<int:pk>/',EmployeeUpdateImage.as_view(),name='employee-update'),
    path('employeeedit/<int:pk>/',EmployeeUpdate.as_view(),name='employee-update')      
]