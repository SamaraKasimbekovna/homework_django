from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Books


def books_detail(request, id):
    books_detail = get_object_or_404(Books, id=id)
    return render(request, "books_detail.html", {"book": books_detail})

    

def books_list(request):
    books = Books.objects.all().order_by("-id")
    return render(request, "books_list.html", {"books": books})



def quotes_view(request):
    return HttpResponse("""
        <h1>Три знаменитые цитаты писателей</h1>
        <ul>
            <li>Конфуций</li>
            <li>Джозеф Аддисон</li>
            <li>Виктор Гюго</li>
        </ul>
    """)


# Create your views here.
