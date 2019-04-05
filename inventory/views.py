import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from inventory.models import InventoryItem, Category

def set_session(request, category):
    if not request.session.exists(request.session.session_key):
        request.session.create()

    request.session['category'] = category
    request.session.modified = True

@csrf_exempt
def change_category(request):
    category_filter = request.POST.get('category')
    category = Category.objects.filter(name__icontains=category_filter).first()

    inventory = InventoryItem.objects.filter(category=category)

    set_session(request, category_filter)

    # Pagination
    paginator = Paginator(inventory, 16)
    page = request.GET.get('page')
    inventory = paginator.get_page(page)
    total_pages = inventory.paginator.num_pages

    if inventory.number + 5 > total_pages:
        page_set = range(inventory.number, total_pages)
    else:
        page_set = range(inventory.number, inventory.number + 4)

    template = 'ajax/filtered_inventory.html'
    context = {
        'inventory': inventory,
        'page_set': page_set
    }

    new_inventory = render_to_string(template, context, request)
    return HttpResponse(json.dumps({'new_inventory': new_inventory}), content_type='application/json')

def inventory_catalog(request):
    template = "catalog.html"

    inventory = InventoryItem.objects.all()
    if request.session.get('category'):
        category = Category.objects.get(name__icontains=request.session.get('category'))
        inventory = inventory.filter(category=category)

    categories = Category.objects.all()

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
        'page_set': page_set,
        'categories': categories,
        "current_page": "catalog"
    }

    return render(request, template, context)
