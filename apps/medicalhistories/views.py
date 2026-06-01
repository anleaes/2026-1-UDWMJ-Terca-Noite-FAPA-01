from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicalHistoryForm
from .models import MedicalHistory
 # Create your views here.

def add_medicalhistory(request):
    template_name = 'medicalhistories/add.html'
    context = {}
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medicalhistories:list_medicalhistories')
    form = MedicalHistoryForm()
    context['form'] = form
    return render(request, template_name, context)
 
def list_medicalhistories(request):
    template_name = 'medicalhistories/list.html'
    histories = MedicalHistory.objects.filter()
    context = {'histories': histories}
    return render(request, template_name, context)
 
def edit_medicalhistory(request, id_medicalhistory):
    template_name = 'medicalhistories/add.html'
    context = {}
    history = get_object_or_404(MedicalHistory, id=id_medicalhistory)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('medicalhistories:list_medicalhistories')
    form = MedicalHistoryForm(instance=history)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_medicalhistory(request, id_medicalhistory):
    history = MedicalHistory.objects.get(id=id_medicalhistory)
    history.delete()
    return redirect('medicalhistories:list_medicalhistories')