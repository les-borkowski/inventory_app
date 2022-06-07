from django.http import Http404, HttpResponse, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Item


def index(request):
    items_list = Item.objects.all()
    context = {'items_list': items_list}
    return render(request, 'inventory/index.html', context)
    # return HttpResponse("Hello, world.")

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'inventory/detail.html', {'item': item})
    

