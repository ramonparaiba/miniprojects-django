from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.item
