from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "phone_number", "email", "address", "notes"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 09171234567"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "Home or office address"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Optional notes"}),
        }
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "phone_number": "Phone number",
            "email": "Email address",
            "address": "Address",
            "notes": "Notes",
        }

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"].strip()
        if not phone:
            raise forms.ValidationError("Phone number is required.")
        return phone
