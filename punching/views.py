# views.py
from django.shortcuts import render, redirect
from employee.models import Employee
from punching.models import Punching
from punching.forms import AttendanceForm

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
