from celery import shared_task
from punching.models import Punching

@shared_task
def calculate_attendance(employee_id):
    employee_attendance = Punching.objects.filter(employee_id=employee_id).order_by('punch_time')
    if employee_attendance.exists():
        first_punch = employee_attendance.first().punch_time
        last_punch = employee_attendance.last().punch_time
    return f"Attendance calculated for Employee ID: {employee_id}"