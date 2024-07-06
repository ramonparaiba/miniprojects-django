from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    items = Item.objects.all()
    context = {'items':items, 'form': form}
    return render(request, 'listbuy/index.html', context)

def edit_item(request, item_id ):
    item = get_object_or_404(Item, id = item_id )
    if request.method == 'POST':
        form = ItemForm (request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=item) 
    
    context = {'form': form, 'item_id': item_id}
    return render(request, 'listbuy/edit_item.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    context = {'item': item}
    return render(request, 'listbuy/delete_item.html', context)