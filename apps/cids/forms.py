from django import forms
from .models import Cid
 
class CidForm(forms.ModelForm):
    
    class Meta:
        model = Cid
        exclude = ()
 