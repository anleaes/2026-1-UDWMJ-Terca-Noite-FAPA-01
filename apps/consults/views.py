from django.shortcuts import render, get_object_or_404, redirect
from .forms import ConsultForm
from .models import Consult
# Create your views here.

 
def add_consult(request):
    template_name = 'consults/add.html'
    context = {}
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('consults:list_consults')
    form = ConsultForm()
    context['form'] = form
    return render(request, template_name, context)
 
def list_consults(request):
    template_name = 'consults/list.html'
    consults = Consult.objects.select_related('patient', 'doctor')
    context = {'consults': consults}
    return render(request, template_name, context)
 
def edit_consult(request, id_consult):
    template_name = 'consults/add.html'
    context = {}
    consult = get_object_or_404(Consult, id=id_consult)
    if request.method == 'POST':
        form = ConsultForm(request.POST, instance=consult)
        if form.is_valid():
            form.save()
            return redirect('consults:list_consults')
    form = ConsultForm(instance=consult)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_consult(request, id_consult):
    consult = Consult.objects.get(id=id_consult)
    consult.delete()
    return redirect('consults:list_consults')
 