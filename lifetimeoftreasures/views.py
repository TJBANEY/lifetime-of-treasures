from django.http import HttpResponse
from django.shortcuts import render

def health_check():
    print("Healthy")
    return HttpResponse("Healthy")

def clear_sort_keys_from_filter(request):
    if request.session.get('category'):
        request.session.pop('category')
    request.modified = True

def landing_page(request):
    template = "landing_page.html"
    clear_sort_keys_from_filter(request)
    context = {
        "current_page": "home"
    }

    return render(request, template, context)