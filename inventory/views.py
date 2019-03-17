from django.shortcuts import render
from django.core.paginator import Paginator

from inventory.models import InventoryItem


def inventory_catalog(request):
    template = "catalog.html"

    inventory = InventoryItem.objects.all()

    # Pagination
    paginator = Paginator(inventory, 16)
    page = request.GET.get('page')
    inventory = paginator.get_page(page)
    total_pages = inventory.paginator.num_pages

    if inventory.number + 5 > total_pages:
        page_set = range(inventory.number, total_pages)
    else:
        page_set = range(inventory.number, inventory.number + 4)

    context = {
        'inventory': inventory,
        'page_set': page_set
    }

    return render(request, template, context)
