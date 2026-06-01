from django import forms
from .models import Prescription
 
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = ()
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4}),
        }
 