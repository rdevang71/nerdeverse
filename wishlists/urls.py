from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_list, name='wishlist_list'),
    path('create/', views.create_wishlist_item, name='create_wishlist_item'),
    path('delete/<int:item_id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('toggle/<int:item_id>/', views.toggle_completion, name='toggle_completion'),
]