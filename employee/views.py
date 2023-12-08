from django.shortcuts import render, get_object_or_404, redirect
from employee.forms import EmployeeForm
from employee.models import Employee

def list_employee(request):
    items = Employee.objects.all().order_by("-id")
    return render(request, 'list.html', {'items': items})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form, 'item': employee})
    
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('list_employee')
    return render(request, 'delete.html', {'employee': employee})

def details_employee(request,pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        return redirect('attendance_list', employee_id=pk)
    return redirect('attendance_list', employee_id=pk)