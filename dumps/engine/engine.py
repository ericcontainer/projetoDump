import os
import django
from django.conf import settings
from dumps.models import Group, Person, Membership


class GerenciaFiles():
	def __init__(self, codigo):
		self.codigo = codigo
		
	def list_dir_by_code(self):
		user_dir = os.listdir(settings.DIRDUMP)
		list_filter_codigo = filter(lambda x: x.rfind(self.codigo) != -1, os.listdir(settings.DIRDUMP))
		return list_filter_codigo
	
	def list_files_by_code(self, dirdump):
		files = os.listdir(dirdump)
		return files
		

class Historico():
	def __init__(self):
		pass


class GerenciaGrupo():
	def __init__(self, codigo):
		self.codigo = codigo
		
	
	def create_grupo(self):
		# cria grupo geral
		novo_grupo = django.contrib.auth.models.Group.objects.get_or_create(name=self.codigo)
		# cria grupo dump
		grupo = Group(name = novo_grupo[0], descricao=self.codigo)
		grupo.save()

	def create_user(self, cpf, user, email):
		ps = django.contrib.auth.models.User.objects.get_or_create(name = user)
		person = Person(name = ps[0], cpf = cpf, user = user, email = email)
		person.save()

	def associa_user_group(self, grupo, user):
		gs = django.contrib.auth.models.Group.objects.filter(name = self.codigo).get()
		grup = Group.objects.filter(name = gs).get()
		ps = django.contrib.auth.models.User.objects.filter(name = user).get()
		person = Person.objects.filter(name = ps).get()
		ms = Membership(person = person, group = grup)
		ms.save()
		
		
				
