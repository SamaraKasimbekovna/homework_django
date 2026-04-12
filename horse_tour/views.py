from django.shortcuts import render
from django.shortcuts import render
from .models import Location


def location_list_view(request):
    if request.method == 'GET':
        locations = Location.objects.all().order_by('-id')
        return render(
            request,
            'location_list.html',
            {
                'locations': locations
            }
        )
# Create your views here.
