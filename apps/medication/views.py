from django.shortcuts import render, redirect, get_object_or_404
from .forms import MedicationForm
from .models import Medication

# Create your views here.
def add_medication(request):
    template_name = 'medication/add_medication.html'
    context = {}
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categories:list_categories')
    form = MedicationForm()
    context['form'] = form
    return render(request, template_name, context)

def list_medication(request):
    template_name = 'medication/list_medication.html'
    medication = Medication.objects.filter()
    context = {
        'medication': medication
    }
    return render(request, template_name, context)

def edit_medication(request, id_medication):
    template_name = 'medication/add_medication.html'
    context ={}
    medication = get_object_or_404(Medication, id=id_medication)
    if request.method == 'POST':
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medication:list_medication')
    form = MedicationForm(instance=medication)
    context['form'] = form
    return render(request, template_name, context)

def delete_medication(request, id_medication):
    medication = Medication.objects.get(id=id_medication)
    medication.delete()
    return redirect('medication:list_medication')