from core.models import BuildPC, Processor, Motherboard, Memory, GraphicCard
from rest_framework.viewsets import ModelViewSet
from .serializers import PcBuilderSerializer,ValidationError, ProcessorSerializer, MotherboardSerializer, MemorySerializer, GraphicCardSerializer 
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
        graphic_card =  request.data.pop('graphic_card')

        if isinstance(processor, list):
            return Response({'Possivel selecionar somente um processador'}, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(motherboard, list):
            return Response({'Possivel selecionar somente uma placa-mae'}, status=status.HTTP_400_BAD_REQUEST)
        elif qty_memory == 0:
            return Response({'Selecionar pelo menos uma memória'}, status=status.HTTP_400_BAD_REQUEST)

        processor = Processor.objects.get(id=processor)
        motherboard = Motherboard.objects.get(id=motherboard)
        if graphic_card is not None:
            graphic_card = GraphicCard.objects.get(id=graphic_card)
        
        support_memory = motherboard.support_memory
        if processor.model not in motherboard.support_processor:
             return Response({'Modelo do processador incompativel com a placa.'}, status=status.HTTP_400_BAD_REQUEST)
        elif qty_memory > motherboard.slots_memory:
            return Response({'Placa suporta somente '+str(motherboard.slots_memory)+' slots de memoria'}, status=status.HTTP_400_BAD_REQUEST)
        elif graphic_card is None and motherboard.integrated_video == False:
            return Response({'Placa-mae necessita obrigatoriamente de uma placa de video.'}, status=status.HTTP_400_BAD_REQUEST)

        mem = []
        size_memory = 0
        for ram in memory:
            mem.append(Memory.objects.get(id=ram))
            size_memory += mem[-1].size
            if size_memory > support_memory:
                return Response({'Placa nao suporta o tamanho total das memorias'}, status=status.HTTP_400_BAD_REQUEST)
        
        pc = BuildPC.objects.create(client=client,processor=processor,motherboard=motherboard,graphic_card=graphic_card)
        pc.memory.set(mem)

        return Response(status=status.HTTP_201_CREATED)