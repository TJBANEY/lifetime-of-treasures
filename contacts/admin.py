from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact