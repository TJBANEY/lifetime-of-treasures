from django.contrib import admin
from django.urls import path

from filebrowser.sites import site

from inventory.views import inventory_catalog
from lifetimeoftreasures.views import landing_page

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('catalog/', inventory_catalog),
    path('', landing_page)
]
