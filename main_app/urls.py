from django.urls import path
from . import views

urlpatterns = [
    # BEFORE CODE
  path('', views.home, name='home'),
# AfterCODE
#   path('', views.WishList.as_view(), name='wish_list'),
  path('add/', views.WishCreate.as_view(), name='add'),
  path('<int:pk>/delete/', views.WishDelete.as_view(), name='wish_delete')
]

# path('cats/', views.CatList.as_view(), name='cats_index'),