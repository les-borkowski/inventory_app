from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=256)
    item_code = models.IntegerField()
    category = models.CharField(max_length=128, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
