from django.shortcuts import get_object_or_404, redirect, render

from .models import Item
from .forms import ItemForm


def list(request):
    items_list = Item.objects.all()
    context = {'items_list': items_list}
    return render(request, 'inventory/index.html', context)


def detail(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=item_id)
        return render(request, 'inventory/detail.html', {'item': item})
    
    
def create(request):
    create_item_form = ItemForm
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'inventory/create.html', {'form': create_item_form})


def update(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
            
    return render(request, 'inventory/update.html', {'item': item, 'form':form})


def delete(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('/')