from django.urls import path
from .views import index

app_name = 'wangwe'
urlpatterns = [
    path('', index, name='home'),
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)