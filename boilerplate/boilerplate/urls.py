from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ! Cannot be found. @see https://stackoverflow.com/questions/47563013/unable-to-import-path-from-django-urls
# from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="Boilerplate API",
        default_version='v0.0.1',
        description="Sample API to boilerplate future services.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="louisandrew3@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('restapi.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]
