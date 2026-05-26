from django.shortcuts import render, redirect, get_object_or_404
from .forms import CIDForm
from .models import CID

# Create your views here.
def add_CID(request):
    template_name = 'CID/add_CID.html'
    context = {}
    if request.method == 'POST':
        form = CIDForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categories:list_categories')
    form = CIDForm()
    context['form'] = form
    return render(request, template_name, context)

def list_CID(request):
    template_name = 'categories/list_CID.html'
    categories = CID.objects.filter()
    context = {
        'CID': CID
    }
    return render(request, template_name, context)

def edit_CID(request, id_CID):
    template_name = 'CID/add_CID.html'
    context ={}
    CID = get_object_or_404(CID, id=id_CID)
    if request.method == 'POST':
        form = CIDForm(request.POST, instance=CID)
        if form.is_valid():
            form.save()
            return redirect('CID:list_CID')
    form = CIDForm(instance=CID)
    context['form'] = form
    return render(request, template_name, context)

def delete_CID(request, id_CID):
    CID = CID.objects.get(id=id_CID)
    CID.delete()
    return redirect('CID:list_CID')