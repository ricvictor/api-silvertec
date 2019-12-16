from django.db import models
from django.core.exceptions import ValidationError

class Processor(models.Model):
    product = models.TextField()
    model = models.TextField()

    def __str__(self):
        return self.product

class Motherboard(models.Model):
    product = models.TextField()
    support_processor = models.TextField()
    slots_memory = models.IntegerField()
    support_memory = models.IntegerField()
    integrated_video = models.BooleanField()
    
    def __str__(self):
        return self.product

class Memory(models.Model):
    product = models.TextField()
    size = models.IntegerField()

    def __str__(self):
        return '%s %dGB' % (self.product, self.size)

class GraphicCard(models.Model):
    product = models.TextField()

class BuildPC(models.Model):
    client = models.TextField()
    processor = models.ForeignKey(Processor, on_delete=models.PROTECT)
    motherboard = models.ForeignKey(Motherboard,on_delete=models.PROTECT)
    memory = models.ManyToManyField(Memory)
    qty_memory = models.IntegerField()
    graphic_card = models.ForeignKey(GraphicCard,on_delete=models.SET_NULL, null=True)
