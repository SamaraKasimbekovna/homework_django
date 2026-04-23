from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Books
from django.views.generic import ListView, DetailView

class BookListView(ListView):
    model = Books
    template_name = "books_list.html"
    context_object_name = "books"
   
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Books.objects.filter(title__icontains=query)
        else:
            return Books.objects.all()
# def book_list(request):
#     query = request.GET.get('q')
    
#     if query:
#         books = Book.objects.filter(title__icontains=query)
#     else:
#         books = Book.objects.all()
    
#     return render(request, 'books/book_list.html', {'books': books})



class BooksDetailView(DetailView):
    model = Books
    template_name = "books_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"

# def books_detail(request, id):
#     books_detail = get_object_or_404(Books, id=id)
#     return render(request, "books_detail.html", {"book": books_detail})

class BooksListView(ListView):
    model = Books
    template_name = "books_list.html"
    context_object_name = "books"
    ordering = ["-id"]

# def books_list(request):
#     books = Books.objects.all().order_by("-id")
#     return render(request, "books_list.html", {"books": books})

