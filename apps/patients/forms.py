from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ()

class PatientCreateForm(forms.ModelForm):
    allergies_text    = forms.CharField(label='Alergias', widget=forms.Textarea, required=False)
    family_history_text = forms.CharField(label='Histórico Familiar', widget=forms.Textarea, required=False)

    class Meta:
        model = Patient
        exclude = ('allergies',)