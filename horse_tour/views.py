from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Location
from django.views.generic import ListView

class LocationListView(ListView):
    model = Location
    template_name = "location_list.html"
    context_object_name = "locations"
    ordering = ["-id"]
    paginate_by = 5



# def location_list_view(request):
#     locations = Location.objects.all().order_by('-id')
#
#     paginator = Paginator(locations, 2)  # по 2 на страницу
    # page = request.GET.get('page')
    # page_obj = paginator.get_page(page)

    # return render(
    #     request,
    #     'location_list.html',
    #     {
    #         'page_obj': page_obj
    #     }
    # )
# Create your views here.
