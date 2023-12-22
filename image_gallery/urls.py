from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

handler404 = 'gallery.views.custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirection, name='redirection'),
    path('gallery/', include('gallery.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
