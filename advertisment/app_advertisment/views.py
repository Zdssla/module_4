from django.shortcuts import render
from .models import Advertisement

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisement': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

