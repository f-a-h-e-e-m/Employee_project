from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    