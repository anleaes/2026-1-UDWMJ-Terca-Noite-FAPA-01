from django.shortcuts import render, get_object_or_404, redirect
from .forms import DoctorForm
from .models import Doctor
 # Create your views here.

def add_doctor(request):
    template_name = 'doctors/add.html'
    context = {}
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('doctors:list_doctors')
    form = DoctorForm()
    context['form'] = form
    return render(request, template_name, context)
 
def list_doctors(request):
    template_name = 'doctors/list.html'
    doctors = Doctor.objects.filter()
    context = {'doctors': doctors}
    return render(request, template_name, context)
 
def edit_doctor(request, id_doctor):
    template_name = 'doctors/add.html'
    context = {}
    doctor = get_object_or_404(Doctor, id=id_doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors:list_doctors')
    form = DoctorForm(instance=doctor)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_doctor(request, id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    doctor.delete()
    return redirect('doctors:list_doctors')
 