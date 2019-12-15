from rest_framework.serializers import ModelSerializer
from core.models import BuildPC

class PcBuilderSerializer(ModelSerializer):
    class Meta:
        model = BuildPC
        fields = ['processor', 'motherboard', 'memory', 'graphic_card']

