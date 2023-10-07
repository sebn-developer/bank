from django.conf.urls.static import static
from bankproject import settings
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)