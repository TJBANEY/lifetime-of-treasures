from django.http import HttpResponse
from django.shortcuts import render

def health_check():
    print("Healthy")
    return HttpResponse("Healthy")

def landing_page(request):
    template = "landing_page.html"
    request.session.clear()

    return render(request, template, {})