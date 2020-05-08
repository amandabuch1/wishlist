from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Wish

# Define the home view
def home(request):
    wishs = Wish.objects.all()
    return render(request, 'home.html', { 'wishs': wishs })


