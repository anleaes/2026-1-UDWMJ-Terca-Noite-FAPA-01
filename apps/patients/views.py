from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PatientForm, PatientCreateForm
from .models import Patient
from medicalhistories.models import MedicalHistory

def add_patient(request):
    template_name = 'patients/add.html'
    if request.method == 'POST':
        form = PatientCreateForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            history = MedicalHistory.objects.create(
                patient_name=patient.name,
                allergies=form.cleaned_data.get('allergies_text', ''),
                family_history=form.cleaned_data.get('family_history_text', ''),
            )
            patient.allergies = history
            patient.save()
            return redirect('patients:list_patients')
    else:
        form = PatientCreateForm()
    return render(request, template_name, {'form': form})
 
def list_patients(request):
    template_name = 'patients/list.html'
    patients = Patient.objects.filter()
    context = {'patients': patients}
    return render(request, template_name, context)
 
def edit_patient(request, id_patient):
    template_name = 'patients/add.html'
    context = {}
    patient = get_object_or_404(Patient, id=id_patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients:list_patients')
    form = PatientForm(instance=patient)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_patient(request, id_patient):
    patient = Patient.objects.get(id=id_patient)
    patient.delete()
    return redirect('patients:list_patients')
 