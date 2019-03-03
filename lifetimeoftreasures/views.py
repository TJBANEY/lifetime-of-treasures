from django.shortcuts import render


def landing_page(request):
    template = "base.html"

    return render(request, template, {})