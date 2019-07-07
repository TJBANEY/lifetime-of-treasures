from django.http import HttpResponse
from django.shortcuts import render

from inventory.models import InventoryItem


def health_check():
    print("Healthy")
    return HttpResponse("Healthy")

def clear_sort_keys_from_filter(request):
    if request.session.get('category'):
        request.session.pop('category')
    request.modified = True

def landing_page(request):
    template = "landing_page.html"

    inventory_preview = InventoryItem.objects.all()[:4]

    clear_sort_keys_from_filter(request)
    context = {
        "current_page": "home",
        "inventory_preview": inventory_preview
    }

    return render(request, template, context)

def temp_estate_sales_view(request):
    template = "temp/estate-sales.html"
    context = {
        "current_page": "estate-sales"
    }

    return render(request, template, context)

def temp_about_us(request):
    template = "temp/about-us.html"
    context = {
        "current_page": "about"
    }

    return render(request, template, context)