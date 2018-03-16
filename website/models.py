from django.db import models
from datetime import datetime

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=100)
	specialization = models.CharField(max_length=50)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50, default='12345')
	
	def __str__(self):
		return self.name


class Pharmacist(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50, default='12345')
	
	def __str__(self):
		return self.name

class Patient(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50, default='12345')
	
	def __str__(self):
		return self.name

class Medicine(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Prescription(models.Model):
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	medicine = models.ManyToManyField(Medicine)

	def __str__(self):
		return self.patient.name


class MedicalHistory(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	disease = models.CharField(max_length=50)
	startDate = models.DateTimeField('Start Date')
	endDate = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.patient.name


class Permission(models.Model):
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	resourceId = models.IntegerField()
	resourceType = models.CharField(max_length=50)
	approved = models.BooleanField(default=False)
	pending = models.BooleanField(default=True)
