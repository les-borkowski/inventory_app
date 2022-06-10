from django.shortcuts import get_object_or_404, redirect, render

from .models import Item, Location
from .forms import ItemForm, LocationForm


def list(request):
    """inventory list view"""
    items_list = Item.objects.all()
    context = {'items_list': items_list}
    return render(request, 'inventory/index.html', context)


def detail(request, item_id):
    """item detail view"""
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=item_id)
        return render(request, 'inventory/detail.html', {'item': item})


def create(request):
    """create item view"""
    create_item_form = ItemForm
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'inventory/create.html', {'form': create_item_form})


def update(request, item_id):
    """edit item view"""
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'inventory/update.html', {'item': item, 'form': form})


def delete(request, item_id):
    """delete item view"""
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('/')


def location_list(request):
    """locations view"""
    locations_list = Location.objects.all()
    add_location_form = LocationForm
    context = {'locations_list': locations_list, 'form': add_location_form}
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/location_list/')
    return render(request, 'inventory/list_locations.html', context)


def delete_location(request, location_id):
    """delete location view"""
    location = Location.objects.get(pk=location_id)
    location.delete()
    return redirect('/location_list/')
