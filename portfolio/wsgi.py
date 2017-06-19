"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import site
import sys

site.addsitedir('/mnt/Data/.virtual/portfolio/lib/python3.5/site-packages')

# Add the app's directory to the PYTHONPATH
#sys.path.append('/home/dio/Projects/portfolio/')
#sys.path.append('/home/dio/Projects/portfolio/portfolio')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings.local")
# Activate your virtual env
#exec(open("/mnt/Data/.virtual/portfolio/bin/activate_this.py").read())

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
