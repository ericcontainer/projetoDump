from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

class Person(models.Model):
	cpf = models.OneToOneField(User, on_delete=models.CASCADE, max_length=11)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	def __str__(self):
		return str(self.cpf)
	
class Group(models.Model):
	
	name = models.OneToOneField(Group, on_delete=models.CASCADE, max_length=5)
	members = models.ManyToManyField(Person, through='Membership')
	descricao = models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.name)

class Membership(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

	date_joined = models.DateField()

	def __str__(self):
		return "User: " + str(self.person) + " Group: " + str(self.group)

class History(models.Model):
	filename = models.CharField(max_length=200)
	download_date = models.DateTimeField(auto_now_add=True, blank=True)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	
