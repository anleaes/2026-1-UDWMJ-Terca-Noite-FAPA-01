from django import forms
from .models import Consult
 
class ConsultForm(forms.ModelForm):
    class Meta:
        model = Consult
        exclude = ()
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'anamnesis':        forms.Textarea(attrs={'rows': 4}),
            'cid':              forms.SelectMultiple(attrs={'size': 6}),
        }
 