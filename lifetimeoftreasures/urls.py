from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from filebrowser.sites import site

from inventory.views import inventory_catalog
from lifetimeoftreasures.views import landing_page

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('catalog/', inventory_catalog),
    path('', landing_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
