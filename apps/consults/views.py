from django.shortcuts import render, get_object_or_404, redirect
from .forms import ConsultForm
from .models import Consult

def add_consult(request):
    template_name = 'consults/add.html'
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            if request.POST.get('exame') == 'S':
                return redirect('exams:add_exam')
            return redirect('consults:list_consults')
    form = ConsultForm()
    return render(request, template_name, {'form': form})

def view_consult(request, id_consult):
    consult = get_object_or_404(Consult.objects.select_related('patient', 'doctor').prefetch_related('cid'), id=id_consult)
    return render(request, 'consults/view.html', {'consult': consult})

def list_consults(request):
    template_name = 'consults/list.html'
    consults = Consult.objects.select_related('patient', 'doctor')
    context = {'consults': consults}
    return render(request, template_name, context)

def edit_consult(request, id_consult):
    template_name = 'consults/add.html'
    consult = get_object_or_404(Consult, id=id_consult)
    if request.method == 'POST':
        form = ConsultForm(request.POST, instance=consult)
        if form.is_valid():
            form.save()
            return redirect('consults:list_consults')
    form = ConsultForm(instance=consult)
    return render(request, template_name, {'form': form})

def delete_consult(request, id_consult):
    consult = Consult.objects.get(id=id_consult)
    consult.delete()
    return redirect('consults:list_consults')
