from django.shortcuts import render

def inventory_catalog(request):
    template = "catalog.html"
    context = {}

    return render(request, template, context)
