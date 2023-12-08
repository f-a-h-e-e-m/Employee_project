from django import forms
from punching.models import Punching

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Punching
        fields = ['employee', 'punch_date', 'punch_time', 'check_in']
        widgets = {
            'punch_date': forms.DateInput(attrs={'type': 'date'}),
            'punch_time': forms.TimeInput(attrs={'type': 'time'}),
        }