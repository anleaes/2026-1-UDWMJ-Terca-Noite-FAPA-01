from django import forms
from .models import Consult

class ConsultForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(
        label='Data/Hora',
        input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )

    class Meta:
        model = Consult
        exclude = ()
        widgets = {
            'anamnesis': forms.Textarea(attrs={'rows': 4}),
            'cid':       forms.CheckboxSelectMultiple(),
        }
 