from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore_home, name='explore_home'),
]