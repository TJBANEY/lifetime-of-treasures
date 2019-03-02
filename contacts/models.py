from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    inquiry = models.TextField(max_length=20000, default='')

    subject = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    responded_to = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"