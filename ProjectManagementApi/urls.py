
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Project Management API",
      default_version='v1',
      description="#",
      terms_of_service="#",
      contact=openapi.Contact(email="sobujhd@gmail.com"),
      license=openapi.License(name="BD"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('project/',include('App_Project.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)