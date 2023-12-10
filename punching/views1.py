# views.py
from django.shortcuts import render, redirect
from employee.models import Employee
from punching.models import Punching
from punching.forms import AttendanceForm
from django.http import JsonResponse
from django.shortcuts import render
from .tasks import calculate_attendance

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('attendance_list',employee_id=obj.employee_id)
    else:
        form = AttendanceForm()
    return render(request, 'add_attendance.html', {'form': form})

def attendance_list(request,employee_id):
    attendances = Punching.objects.filter(employee_id=employee_id).order_by('-punch_date')
    return render(request, 'attendance_list.html', {'attendances': attendances})

def attendance_report(request, employee_id):
    calculate_attendance.delay(employee_id)
    return render(request, 'attendance_report.html', {'employee_id': employee_id})

def get_attendance_details(request):
    # Get the latest attendance details for the specified employee
    employee_id = request.GET.get('employee_id')
    employee_attendance = Punching.objects.filter(employee_id=employee_id).order_by('punch_time')
    # Example: Extract first and last punches
    first_punch = employee_attendance.first().punch_time if employee_attendance.exists() else None
    last_punch = employee_attendance.last().punch_time if employee_attendance.exists() else None
    # Construct a JSON response with the attendance details
    response_data = {
        'first_punch': str(first_punch),
        'last_punch': str(last_punch),
    }
    return JsonResponse(response_data)