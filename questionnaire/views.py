from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm
from django.shortcuts import get_object_or_404

def questionnaire_detail(request, pk):
    questionnaire = get_object_or_404(Questionnaire, pk=pk)
    
    questionnaire.views += 1
    questionnaire.save()

    return render(request, 'questionnaire/detail.html', {'questionnaire': questionnaire})

# список анкет
def questionnaire_list(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'questionnaire/list.html', {'questionnaires': questionnaires})


# создание
def questionnaire_create(request):
    form = QuestionnaireForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('questionnaire:list')
    return render(request, 'questionnaire/form.html', {'form': form})


# обновление
def questionnaire_update(request, pk):
    obj = get_object_or_404(Questionnaire, pk=pk)
    form = QuestionnaireForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('questionnaire:list')
    return render(request, 'questionnaire/form.html', {'form': form})


# удаление
def questionnaire_delete(request, pk):
    obj = get_object_or_404(Questionnaire, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('questionnaire:list')
    return render(request, 'questionnaire/delete.html', {'obj': obj})

# Create your views here.
