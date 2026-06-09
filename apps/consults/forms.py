from django import forms
from .models import Consult
from cids.models import Cid

class CidMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} - {obj.description}"

class ConsultForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(
        label='Data/Hora',
        input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )
    cid = CidMultipleChoiceField(
        queryset=Cid.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='CIDs',
    )

    class Meta:
        model = Consult
        exclude = ()
        widgets = {
            'anamnesis': forms.Textarea(attrs={'rows': 4}),
        }
 