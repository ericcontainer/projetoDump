import os
import mimetypes
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.conf import settings
from .models import Person, Membership
from engine import engine
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from sendfile import sendfile

MENUADMIN = ['Criar Grupo', 'Criar Usuario']
MENUUSER = ['Meus Dumps']

def checkMenu(request):
	user = request.user
	if user.groups.filter(name = 'administracao').exists():
		menu = MENUADMIN
	else:
		menu = MENUUSER
	return menu

#def serve_using_xsendfile(request, hash, path, filename):
def serve_using_xsendfile(request, path, filename):
	if request.user.is_authenticated:
		file_full_path = os.path.join(settings.DIRDUMP,path, filename)
		print file_full_path


#		with open(file_full_path,'r') as f:
#			data = f.read()

#		print hash
		print path
		print filename
		response = HttpResponse()
#		response = HttpResponse(data, content_type=mimetypes.guess_type(file_full_path)[0])
#		response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
#		response['Content-type'] = 'application/octet-stream'
#		response['X-Sendfile'] = '/home/eric/Documentos/dumps/BSA_AP_84006_PRO_SIGPB/Django'
		response['X-Accel-Redirect'] = file_full_path
#		response['Content-Length'] = os.path.getsize(file_full_path)
		return response
#		return sendfile(request, file_full_path, attachment=True)
	else:
		return HttpResponseForbidden()


@login_required(login_url="login/")
def home(request):
	return render(request,"home.html", {'menu':checkMenu(request)})

@login_required(login_url="login/")
def adminView(request):
    return HttpResponse("Visao do admin")

@login_required(login_url="login/")
def clienteView(request):
	
	gpsuser = Membership.objects.filter(person = Person.objects.filter(cpf = request.user))
	
	dirsfiles = {}
	for g in gpsuser:
		print dir(g)
		dump_user = engine.GerenciaFiles(g.group.name.name)
		context = dump_user.list_dir_by_code()	
		for x in context:
			dirsfiles[x] = dump_user.list_files_by_code(settings.DIRDUMP+"/"+x)
	print dirsfiles
	value = request.GET
	print dir(value.values)
	return render(request, 'clienteview.html', {'dirs': dirsfiles,'menu':checkMenu(request)})

@staff_member_required
def media_xsendfile(request, path, document_root):
    response = HttpResponse()
    response['Content-Type'] = ''
    response['X-Sendfile'] = (os.path.join(settings.MEDIA_ROOT, path)).encode('utf-8')
    return response
