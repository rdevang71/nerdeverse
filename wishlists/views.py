from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import WishlistItemForm
from .models import WishlistItem

@login_required
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
    return render(request, 'create.html', {'form': form})

@login_required
def wishlist_list(request):
    items = WishlistItem.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'wishlist.html', {'items': items})

@login_required
def delete_wishlist_item(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    item.delete()
    return redirect('wishlist_list')

@login_required
def toggle_completion(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    item.is_completed = not item.is_completed
    item.save()
    return redirect('wishlist_list')