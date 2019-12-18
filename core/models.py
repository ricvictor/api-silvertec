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
    product = models.TextField(null=True)
    size = models.IntegerField()

    def __str__(self):
        return '%s %dGB' % (self.product, self.size)

class GraphicCard(models.Model):
    product = models.TextField()

class BuildPC(models.Model):
    client = models.TextField(null=True)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard,on_delete=models.CASCADE)
    memory = models.ManyToManyField(Memory)
    graphic_card = models.ForeignKey(GraphicCard,on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('client',)