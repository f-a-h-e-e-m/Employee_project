from django.urls.conf import path
from punching.views import add_attendance,attendance_list


urlpatterns = [
    path('attendance/list/<int:employee_id>', attendance_list, name='attendance_list'),
    path('attendance/add', add_attendance, name='add_attendance'),
]