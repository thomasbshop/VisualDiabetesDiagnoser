from django.db import models
# from .models import File

class File(models.Model):
	file = models.FileField(blank=False, null=False)
	name = models.CharField(max_length=20, default='filename')
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.file.name