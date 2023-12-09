from django.urls.conf import path
from punching.views import add_attendance,attendance_list,attendance_report,get_attendance_details


urlpatterns = [
    path('attendance/list/<int:employee_id>', attendance_list, name='attendance_list'),
    path('attendance/add', add_attendance, name='add_attendance'),
    
    path('attendance-report/<int:employee_id>/', attendance_report, name='attendance_report'),
    path('ajax/get_attendance_details/', get_attendance_details, name='get_attendance_details')
]