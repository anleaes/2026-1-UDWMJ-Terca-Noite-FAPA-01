from django import forms
from .models import CID

class CIDForm(forms.ModelForm):

    class Meta:
        model = CID
        exclude = ()