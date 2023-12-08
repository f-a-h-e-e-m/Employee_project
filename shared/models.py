from django.db import models
from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
	def pre_save(self, model_instance, add):
		return timezone.now()

class BaseModel(models.Model):
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = AutoDateTimeField(default=timezone.now)

	class Meta:
		abstract = True