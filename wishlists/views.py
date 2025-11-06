from django.shortcuts import render, redirect
from .forms import WishlistItemForm
from .models import WishlistItem

def create_wishlist_item(request):
    if request.method == 'POST':
        form = WishlistItemForm(request.POST, request.FILES)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.save()
            return redirect('wishlist_list')
    else:
        form = WishlistItemForm()
    return render(request, 'wishlists/create.html', {'form': form})

def wishlist_list(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlists/list.html', {'items': items})