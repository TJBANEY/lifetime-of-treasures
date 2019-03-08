from django.http import HttpResponse
from django.shortcuts import render

def inventory_catalog(request):
    return HttpResponse("INVENTORY")
