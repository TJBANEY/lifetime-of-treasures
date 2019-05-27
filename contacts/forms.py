from django import forms

from contacts.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['inquiry'].required = True
        self.fields['subject'].required = True

    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "phone", "inquiry", "subject"]