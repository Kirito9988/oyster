from django.shortcuts import render
from .models import OysterPackage
from .forms import OysterPackageForm
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'oyster_tracker/index.html')


def upload(request):
    if request.method == 'POST':
        form = OysterPackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OysterPackageForm()
    return render(request, 'oyster_tracker/upload.html', {'form': form})


def tracker(request):
    search_date = request.GET.get('search_date', None)
    packages = []
    if search_date:
        try:
            # Try to convert the search_date string to a date object
            search_date_obj = datetime.strptime(search_date, "%Y-%m-%d").date()
            packages = OysterPackage.objects.filter(harvest_date=search_date_obj)
        except ValueError:
            # If the search_date string is not in the correct format, an error will be raised
            pass
    return render(request, 'oyster_tracker/tracker.html', {'packages': packages})
