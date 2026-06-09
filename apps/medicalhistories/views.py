from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicalHistoryForm
from .models import MedicalHistory

def add_medicalhistory(request):
    template_name = 'medicalhistories/add.html'
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medicalhistories:list_medicalhistories')
    form = MedicalHistoryForm()
    return render(request, template_name, {'form': form})

def list_medicalhistories(request):
    template_name = 'medicalhistories/list.html'
    histories = MedicalHistory.objects.filter()
    context = {'histories': histories}
    return render(request, template_name, context)

def edit_medicalhistory(request, id_medicalhistory):
    template_name = 'medicalhistories/add.html'
    history = get_object_or_404(MedicalHistory, id=id_medicalhistory)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('medicalhistories:list_medicalhistories')
    form = MedicalHistoryForm(instance=history)
    return render(request, template_name, {'form': form})

def delete_medicalhistory(request, id_medicalhistory):
    history = MedicalHistory.objects.get(id=id_medicalhistory)
    history.delete()
    return redirect('medicalhistories:list_medicalhistories')
