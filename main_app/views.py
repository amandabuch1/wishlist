from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView

from django.http import HttpResponse
from .models import Wish

# Define the home view
def home(request):
    wishs = Wish.objects.all()
    return render(request, 'home.html', { 'wishs': wishs })


class WishCreate(CreateView):
  model = Wish
  fields = '__all__'
  success_url = '/'


class WishDelete(DeleteView):
  model = Wish
  success_url = '/'