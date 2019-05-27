from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "created_at", "responded_to")

    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "created_at",
        "inquiry",
        "subject",
    )
    model = Contact