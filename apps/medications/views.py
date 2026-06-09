from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicationForm
from .models import Medication

def add_medication(request):
    template_name = 'medications/add.html'
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medications:list_medications')
    form = MedicationForm()
    return render(request, template_name, {'form': form})

def list_medications(request):
    template_name = 'medications/list.html'
    medications = Medication.objects.filter()
    context = {'medications': medications}
    return render(request, template_name, context)

def edit_medication(request, id_medication):
    template_name = 'medications/add.html'
    medication = get_object_or_404(Medication, id=id_medication)
    if request.method == 'POST':
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medications:list_medications')
    form = MedicationForm(instance=medication)
    return render(request, template_name, {'form': form})

def delete_medication(request, id_medication):
    medication = Medication.objects.get(id=id_medication)
    medication.delete()
    return redirect('medications:list_medications')
