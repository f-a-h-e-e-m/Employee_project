from django.db import models
from shared.models import BaseModel
from employee.models import Employee

# Create your models
class Punching(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='punching_details')
    punch_date = models.DateField()
    punch_time = models.TimeField()
    check_in = models.BooleanField(default=True)
    class Meta:
        db_table = "punching"
        unique_together = ['employee', 'punch_date', 'punch_time']
