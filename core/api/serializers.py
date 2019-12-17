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

    def create_memory(self, memory, pc):
        for ram in memory:
            mem = Memory.objects.create(**ram)
            pc.memory.add(mem)

    def validate(self, attrs):
        processor = attrs['processor']
        motherboard = attrs['motherboard']
        memory = attrs['memory']
        graphic_card = attrs['graphic_card']

        if processor['model'] != motherboard['support_processor']:
            raise ValidationError("Modelo do processador incompativel com a placa.")

        return attrs

    class Meta:
        model = BuildPC
        fields = ['id','client', 'processor', 'motherboard', 'memory', 'qty_memory', 'graphic_card']

