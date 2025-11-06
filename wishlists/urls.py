from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_wishlist_item, name='create_wishlist'),
    path('', views.wishlist_list, name='wishlist_list'),
]