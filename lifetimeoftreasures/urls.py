from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from contacts.views import contact_form
from filebrowser.sites import site

from inventory.views import inventory_catalog, change_category
from lifetimeoftreasures.views import landing_page

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('catalog/', inventory_catalog),
    path('contact/', contact_form),
    path('filter-change', change_category),
    path('', landing_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
