from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
	sentby=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sentby")
	sentto=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sentto")
	file = models.FileField(blank=False, null=False)
	def __str__(self):
		return self.file.name

