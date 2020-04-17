from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from main import views as main_views


urlpatterns = [
    path('', main_views.index, name='index'),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG :
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)