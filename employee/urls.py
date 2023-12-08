from django.urls.conf import path
from employee.views import add_employee,list_employee,update_employee,delete_employee,details_employee


urlpatterns = [
    path('', list_employee, name='list_employee'),
    path('employee/add/',add_employee , name='add_employee'),
    path('employee/edit/<int:pk>',update_employee , name='update_employee'),
    path('employee/delete/<int:pk>',delete_employee , name='delete_employee'),
    path('employee/details/<int:pk>',details_employee , name='details_employee'),
]