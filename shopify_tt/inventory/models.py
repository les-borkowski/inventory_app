from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=256)
    item_code = models.IntegerField()
    category = models.CharField(max_length=128, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
