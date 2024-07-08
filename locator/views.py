from django.shortcuts import render
from .forms import AddressForm
from .models import DistanceSearch
from .utils import find_distance

def index(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            source_address = form.cleaned_data['source_address']
            destination_address = form.cleaned_data['destination_address']
            try:
                distance = find_distance(source_address, destination_address)
            except:
                return render(request, 'locator/error.html')
            DistanceSearch.objects.create(
                source_address=source_address,
                destination_address=destination_address,
                distance_km=distance
            )
            return render(request, 'locator/distance.html', {"distance": distance})
    else:
        form = AddressForm()
    return render(request, 'locator/index.html', {"form": form})

def history(request):
    searches = DistanceSearch.objects.all().order_by('-search_date')
    return render(request, 'locator/history.html', {'searches': searches})