from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import permissions
from os import environ

# ! Cannot be found. @see https://stackoverflow.com/questions/47563013/unable-to-import-path-from-django-urls
# from django.urls import path

app_name = environ.get('DJANGO_APP_NAME', default="local")

protocol = 'http' if environ.get('DEBUG', default=1) == 1 else 'https'
docs_base_url = app_name + '.herokuapp.com' if app_name != "local" else 'localhost:8000'
docs_url = protocol + "://" + docs_base_url + "/api/v1"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('restapi.urls')),
]
