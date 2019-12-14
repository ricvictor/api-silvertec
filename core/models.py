from django.db import models

processor_options = [
            ( 'Intel', 'Processador Intel Core i5'), 
            ( 'Intel', 'Processador Intel Core i7'),
            ('AMD', 'Processador AMD Athlon'),
            ('AMD', 'Processador AMD Ryzen 7')
            ]
motherboard_options = [
            ('Placa Mãe Asus  Prime','Intel', 2, 16, 'Não')
            ]

class Processor(models.Model):
    product = models.TextField()
    model = models.TextField()

class Motherboard(models.Model):
    product = models.TextField()
    support_processor = models.TextField()
    slots_memory = models.IntegerField(max_length=1)
    support_memory = models.IntegerField()
    integrated_video = models.BooleanField()

class Memory(models.Model):
    product = models.TextField
    size = models.IntegerField()

class GraphicCard(models.Model):
    product = models.TextField()

class BuildPC(models.Model):
    processor = models.ForeignKey(Processor,on_delete=models.PROTECT)
    motherboard = models.ForeignKey(Motherboard,on_delete=models.PROTECT)
    memory = models.ManyToManyField(Memory)
    graphic_card = models.ForeignKey(GraphicCard,on_delete=models.SET_NULL, null=True)