from rest_framework.serializers import ModelSerializer, ValidationError
from core.models import Processor, Motherboard, Memory, GraphicCard, BuildPC

class ProcessorSerializer(ModelSerializer):
    class Meta:
        model = Processor
        fields = ['product', 'model']

class MotherboardSerializer(ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['product','support_processor','slots_memory','support_memory', 'integrated_video' ]

class MemorySerializer(ModelSerializer):
    class Meta:
        model = Memory
        fields = ['product','size']

class GraphicCardSerializer(ModelSerializer):
    class Meta:
        model = GraphicCard
        fields = ['product']

class PcBuilderSerializer(ModelSerializer):
    processor = ProcessorSerializer()
    motherboard = MotherboardSerializer()
    memory = MemorySerializer(many=True)
    graphic_card = GraphicCardSerializer()

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
            raise ValidationError("finish must occur after start")

        return attrs

    def create(self, validated_data):
        memory = validated_data['memory']
        del validated_data['memory']

        motherboard = validated_data['motherboard']
        del validated_data['motherboard']

        processor = validated_data['processor']
        del validated_data['processor']

        graphic_card = validated_data['graphic_card']
        del validated_data['graphic_card']

        pc = BuildPC.objects.create(**validated_data)
        self.create_memory(memory,pc)

        pc.processor = processor
        pc.motherboard = motherboard
        pc.graphic_card = graphic_card

        return pc


    class Meta:
        model = BuildPC
        fields = ['client', 'processor', 'motherboard', 'memory', 'graphic_card']

