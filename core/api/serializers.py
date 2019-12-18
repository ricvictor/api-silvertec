from rest_framework.serializers import ModelSerializer, ValidationError, RelatedField
from core.models import Processor, Motherboard, Memory, GraphicCard, BuildPC

class ProcessorSerializer(RelatedField):
   
    def to_representation(self, value):
        return value.product    

class MotherboardSerializer(RelatedField):
    
    def to_representation(self, value):
        return value.product

class MemorySerializer(RelatedField):
    
    def to_representation(self, value):
        return '%s %dGB' % (value.product, value.size)

class GraphicCardSerializer(RelatedField):

    def to_representation(self, value):
        return value.product


class PcBuilderSerializer(ModelSerializer):

    processor = ProcessorSerializer(read_only=True)
    motherboard = MotherboardSerializer(read_only=True)
    memory = MemorySerializer(many=True,read_only=True)
    graphic_card = GraphicCardSerializer(read_only=True)
    
    class Meta:
        model = BuildPC
        fields = ['id','client', 'processor', 'motherboard', 'memory',  'graphic_card']

