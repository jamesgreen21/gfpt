from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from main import views as main_views
from calculator import views as calc_views
from marketing import views as mark_views


urlpatterns = [
    path('', main_views.index, name='index'),
    path('calorie-calculator/', calc_views.index, name='calc'),
    path('subscribe/', mark_views.email_list_subscription, name='subscribe'),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG :
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
