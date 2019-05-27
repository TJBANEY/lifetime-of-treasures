from django.shortcuts import render
from django.contrib import messages

from contacts.forms import ContactForm

def contact_form(request):
    template = 'contacts/contact.html'
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            new_contact = form.save()
            msg = "We received your message, and will get back to you as soon as possible!"
            messages.add_message(request, messages.SUCCESS, msg)
        else:
            form.initial = form.data

    context = {"form": form}
    return render(request, template,  context)