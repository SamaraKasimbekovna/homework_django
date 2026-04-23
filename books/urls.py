from django.urls import path
from .views import (
    BooksListView,
    BooksDetailView
)

urlpatterns = [
    path("", BooksListView.as_view(), name="books_list"),
    path("<int:id>/", BooksDetailView.as_view(), name="books_detail"),
]