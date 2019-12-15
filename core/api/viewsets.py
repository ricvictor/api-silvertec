from core.models import BuildPC
from rest_framework.viewsets import ModelViewSet
from .serializers import PcBuilderSerializer

class PcBuilderViewSet(ModelViewSet):
    queryset = BuildPC.objects.all()
    serializer_class = PcBuilderSerializer