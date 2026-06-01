from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from .forms import PrescriptionForm
from .models import Prescription
from prescriptionitems.models import PrescriptionItem

# Create your views here.
PrescriptionItemFormSet = inlineformset_factory(
    Prescription, PrescriptionItem,
    fields=['medication', 'quantity', 'dosage', 'frequency', 'duration'],
    extra=1, can_delete=True
)
 
def add_prescription(request):
    template_name = 'prescriptions/add.html'
    context = {}
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        formset = PrescriptionItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            prescription = form.save()
            formset.instance = prescription
            formset.save()
            return redirect('prescriptions:list_prescriptions')
    form = PrescriptionForm()
    formset = PrescriptionItemFormSet()
    context['form'] = form
    context['formset'] = formset
    return render(request, template_name, context)
 
def list_prescriptions(request):
    template_name = 'prescriptions/list.html'
    prescriptions = Prescription.objects.select_related('patient', 'doctor')
    context = {'prescriptions': prescriptions}
    return render(request, template_name, context)
 
def edit_prescription(request, id_prescription):
    template_name = 'prescriptions/add.html'
    context = {}
    prescription = get_object_or_404(Prescription, id=id_prescription)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        formset = PrescriptionItemFormSet(request.POST, instance=prescription)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('prescriptions:list_prescriptions')
    form = PrescriptionForm(instance=prescription)
    formset = PrescriptionItemFormSet(instance=prescription)
    context['form'] = form
    context['formset'] = formset
    return render(request, template_name, context)
 
def delete_prescription(request, id_prescription):
    prescription = Prescription.objects.get(id=id_prescription)
    prescription.delete()
    return redirect('prescriptions:list_prescriptions')
 