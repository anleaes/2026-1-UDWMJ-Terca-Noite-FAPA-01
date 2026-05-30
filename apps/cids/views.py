from django.shortcuts import render, redirect, get_object_or_404

from .forms import CidForm
from .models import Cid

# Create your views here.
def add_cid(request):
    template_name = 'cids/add_cid.html'
    context = {}
    if request.method == 'POST':
        form = CidForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cids:list_cids')
    form = CidForm()
    context['form'] = form
    return render(request, template_name, context)

def list_cids(request):
    template_name = 'cids/list_cids.html'
    cids = Cid.objects.filter()
    context = {
        'cids': cids
    }
    return render(request, template_name, context)

def edit_cid(request, id_cid):
    template_name = 'cids/add_cid.html'
    context ={}
    cid = get_object_or_404(Cid, id=id_cid)
    if request.method == 'POST':
        form = CidForm(request.POST, instance=cid)
        if form.is_valid():
            form.save()
            return redirect('cids:list_cids')
    form = CidForm(instance=cid)
    context['form'] = form
    return render(request, template_name, context)

def delete_cid(request, id_cid):
    cid = Cid.objects.get(id=id_cid)
    cid.delete()
    return redirect('cids:list_cids')
