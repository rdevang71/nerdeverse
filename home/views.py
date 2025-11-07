# home/views.py
from django.shortcuts import render
from wishlists.models import WishlistItem  # import your model

def homepage(request):
    all_items = WishlistItem.objects.select_related('user', 'category').order_by('-created_at')
    return render(request, 'index.html', {'wishlist_items': all_items})