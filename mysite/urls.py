from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('blog.urls')),
    path('api-token-auth/', obtain_auth_token),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
