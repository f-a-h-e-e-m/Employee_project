from django.db import models
from shared.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Employee(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hire_date = models.DateField()
    employee_code=models.CharField(max_length=150,blank=True,null=True,unique=True)
    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return f"{self.employee_code} - {self.first_name} {self.last_name}"

@receiver(post_save, sender=Employee)
def create_employee_code(created,instance,**kwargs):
	if created:
		common_code = "000"
		codes = str(int(common_code) + instance.id )
		code_length = len(codes)
		if code_length < 5: # 8 is the max length of your code
			code = "0" * (5 - code_length) + codes
		else:
			code=codes
		title="EMP"
		slug= f'{title}{code}'
		if instance.employee_code != slug:
			Employee.objects.filter(id=instance.id).update(employee_code=slug)
			instance.refresh_from_db()