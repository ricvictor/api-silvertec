from core.models import BuildPC, Processor, Motherboard, Memory, GraphicCard
from rest_framework.viewsets import ModelViewSet
from .serializers import PcBuilderSerializer, ProcessorSerializer, MotherboardSerializer, MemorySerializer, GraphicCardSerializer 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response


class PcBuilderViewSet(ModelViewSet):
    
    queryset = BuildPC.objects.all()
    serializer_class = PcBuilderSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        
        queryset = BuildPC.objects.all()
        client = self.request.query_params.get('client', None)
        
        if client is not None:
            queryset = queryset.filter(client=client)
        return queryset
    
    def create(self,request):
        client = request.data.pop('client')
        processor = request.data.pop('processor')
        motherboard = request.data.pop('motherboard')
        memory = request.data.pop('memory')
        qty_memory = len(memory)
        gp =  request.data.pop('graphic_card')
        processor = Processor.objects.get(id=processor)
        motherboard = Motherboard.objects.get(id=motherboard)
        graphic_card = GraphicCard.objects.get(id=gp)

        if processor.model != motherboard.support_processor:
             return Response({'Modelo do processador incompativel com a placa.'}, status=status.HTTP_400_BAD_REQUEST)

        pc = BuildPC.objects.create(client=client,processor=processor,motherboard=motherboard,graphic_card=graphic_card,qty_memory=qty_memory)
        for ram in memory:
            mem = Memory.objects.get(id=ram)
            pc.memory.add(mem)

        return Response(status=status.HTTP_201_CREATED)