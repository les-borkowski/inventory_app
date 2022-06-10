from django.forms import ModelForm
from .models import Item, Location


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_code', 'category', 'location']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
