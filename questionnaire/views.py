from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm

# список анкет
def questionnaire_list(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'list.html', {'questionnaires': questionnaires})


# создание
def questionnaire_create(request):
    form = QuestionnaireForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'form.html', {'form': form})


# обновление
def questionnaire_update(request, pk):
    obj = get_object_or_404(Questionnaire, pk=pk)
    form = QuestionnaireForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'form.html', {'form': form})


# удаление
def questionnaire_delete(request, pk):
    obj = get_object_or_404(Questionnaire, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('list')
    return render(request, 'delete.html', {'obj': obj})

# Create your views here.
