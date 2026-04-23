from django.urls import path
from .views import (
    QuestionnaireListView,
    QuestionnaireCreateView,
    QuestionnaireUpdateView,
    QuestionnaireDeleteView,
    QuestionnaireDetailView,
)

app_name = 'questionnaire'

urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='list'),
    path('create/', QuestionnaireCreateView.as_view(), name='create'),
    path('update/<int:pk>/', QuestionnaireUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', QuestionnaireDeleteView.as_view(), name='delete'),
    path('<int:pk>/', QuestionnaireDetailView.as_view(), name='detail'),
]