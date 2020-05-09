from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView

from django.http import HttpResponse
from .models import Wish

# Define the home view
# Before code
def home(request):
    wishs = Wish.objects.all()
    return render(request, 'home.html', { 'wishs': wishs })

# AfterCODE
# class WishList(ListView):
#     model = Wish
#     wishs = Wish.objects.all()

#     def get_queryset(self):
#         return wishs

class WishCreate(CreateView):
  model = Wish
  fields = '__all__'
  success_url = '/'


class WishDelete(DeleteView):
  model = Wish
  success_url = '/'


#   class CatList(ListView):
#     model = Cat

#     def get_queryset(self):
#         return Cat.objects.all()