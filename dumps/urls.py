from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'adminview', views.adminView, name = 'adminView'),
	url(r'Meus Dumps', views.clienteView, name = 'clienteview'),
#	url(r'dump(?P<hash>)(?P<path>)(?P<filename>)', views.serve_using_xsendfile, name = 'download'),
	#url(r'^dump/(?P<hash>\d+)/(?P<path>\w+)/(?P<filename>\w+)$', views.serve_using_xsendfile, name = 'download'),
	url(r'(?P<path>\w+)/(?P<filename>\w.*)', views.serve_using_xsendfile, name = 'download'),
#	url(r'^media\/(?P<path>.*)$', 'views.media_xsendfile', {'document_root': settings.MEDIA_ROOT,}),

]
