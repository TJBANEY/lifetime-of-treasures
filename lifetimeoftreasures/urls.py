from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from contacts.views import contact_form
from filebrowser.sites import site

from inventory.views import inventory_catalog, change_category, fetch_single_product_info
from lifetimeoftreasures.views import landing_page, temp_estate_sales_view, temp_about_us

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('catalog/<item_id>', fetch_single_product_info),
    path('catalog/', inventory_catalog),
    path('contact/', contact_form),
    path('estate-sales/', temp_estate_sales_view),
    path('about-us/', temp_about_us),
    path('filter-change', change_category),
    path('', landing_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
