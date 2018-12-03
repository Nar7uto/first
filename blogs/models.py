from django.db import models

# Create your models here.

Class SignUp(models.Model):
	email = models.EmailField()
	fullname = models.CharField()
	timestamp = models.DateTimeField()
	updated = models.DateTimeField()

	def __str__(self):
		return self.email

