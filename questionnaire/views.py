# from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

class QuestionnaireDetailView(DetailView):
    model = Questionnaire
    template_name = "questionnaire/detail.html"
    context_object_name = "questionnaire"

    def get_object(self):
        object = super().get_object()
        object.views += 1
        object.save()
        return object
  

# def questionnaire_detail(request, pk):
#     questionnaire = get_object_or_404(Questionnaire, pk=pk)
    
#     questionnaire.views += 1
#     questionnaire.save()

#     return render(request, 'questionnaire/detail.html', {'questionnaire': questionnaire})

# список анкет
class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = "questionnaire/list.html"
    context_object_name = "questionnaires"

# def questionnaire_list(request):
#     questionnaires = Questionnaire.objects.all()
#     return render(request, 'questionnaire/list.html', {'questionnaires': questionnaires})


# создание
class QuestionnaireCreateView(CreateView):
    model = Questionnaire
    form_class = QuestionnaireForm
    template_name = "questionnaire/form.html"
    success_url = reverse_lazy("questionnaire:list")

# def questionnaire_create(request):
#     form = QuestionnaireForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('questionnaire:list')
#     return render(request, 'questionnaire/form.html', {'form': form})


# обновление
class QuestionnaireUpdateView(UpdateView):
    model = Questionnaire
    form_class = QuestionnaireForm
    template_name = "questionnaire/form.html"
    success_url = reverse_lazy("questionnaire:list")

# def questionnaire_update(request, pk):
#     obj = get_object_or_404(Questionnaire, pk=pk)
#     form = QuestionnaireForm(request.POST or None, request.FILES or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('questionnaire:list')
#     return render(request, 'questionnaire/form.html', {'form': form})


# удаление
class QuestionnaireDeleteView(DeleteView):
    model = Questionnaire
    template_name = "questionnaire/delete.html"
    success_url = reverse_lazy("questionnaire:list")

# def questionnaire_delete(request, pk):
#     obj = get_object_or_404(Questionnaire, pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('questionnaire:list')
#     return render(request, 'questionnaire/delete.html', {'obj': obj})

# Create your views here.
