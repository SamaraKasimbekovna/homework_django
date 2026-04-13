from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaire_list, name='list'),
    path('create/', views.questionnaire_create, name='create'),
    path('update/<int:pk>/', views.questionnaire_update, name='update'),
    path('delete/<int:pk>/', views.questionnaire_delete, name='delete'),
]