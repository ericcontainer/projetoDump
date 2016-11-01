"""
WSGI config for projetoDump project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
#import sys
#import site
from django.core.wsgi import get_wsgi_application
#envpath = '/home/eric/programas/virtualenvProjetoDump/lib/python2.7/site-packages/'
#sys.path.append('/home/eric/programas/projetoDump')
#sys.path.append('/home/eric/programas/projetoDump/projetoDump')
#pwd = os.path.dirname(os.path.abspath(__file__))
#os.chdir(pwd) 

#sys.path = [pwd] + sys.path

#site.addsitedir(envpath)
#from django.core.handlers.wsgi import WSGIHandler
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoDump.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
#application = WSGIHandler()
