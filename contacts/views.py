from django.shortcuts import render

# Create your views here.

def contact_form(request):
    template = 'contacts/contact.html'
    context = {}

    return render(request, template,  context)