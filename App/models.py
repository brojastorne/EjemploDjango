from django.db import models

# Create your models here.


class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=30)
	amo = models.ForeignKey(Person, on_delete=models.CASCADE)
