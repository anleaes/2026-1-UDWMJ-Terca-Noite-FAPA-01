from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExamForm
from .models import Exam

def add_exam(request):
    template_name = 'exams/add.html'
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('exams:list_exams')
    form = ExamForm()
    return render(request, template_name, {'form': form})

def list_exams(request):
    template_name = 'exams/list.html'
    exams = Exam.objects.select_related('consult')
    context = {'exams': exams}
    return render(request, template_name, context)

def edit_exam(request, id_exam):
    template_name = 'exams/add.html'
    exam = get_object_or_404(Exam, id=id_exam)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exams:list_exams')
    form = ExamForm(instance=exam)
    return render(request, template_name, {'form': form})

def delete_exam(request, id_exam):
    exam = Exam.objects.get(id=id_exam)
    exam.delete()
    return redirect('exams:list_exams')
