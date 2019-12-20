from django.urls import include, path
from core.models import Processor, Motherboard, Memory, GraphicCard, BuildPC
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient, URLPatternsTestCase
from django.core.management import call_command

class BuildPCTests(APITestCase):
    
    def test_create_pc(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 2,
                 "motherboard": 12,
                 "memory": [23, 22],
                 "graphic_card": 31
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BuildPC.objects.count(), 1)
        self.assertEqual(BuildPC.objects.get().client, 'Teste')

    def test_incompatible_processor(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 3,
                 "motherboard": 10,
                 "memory": [23, 22],
                 "graphic_card": 31
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{"Modelo do processador incompativel com a placa."})  

    def test_qty_memory(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 2,
                 "motherboard": 10,
                 "memory": [23, 22, 23],
                 "graphic_card": 31
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{'Placa suporta somente 2 slots de memoria'})    

    def test_graphiccard_requirement(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 2,
                 "motherboard": 10,
                 "memory": [23, 22],
                 "graphic_card": None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{'Placa-mae necessita obrigatoriamente de uma placa de video.'})

    def test_size_memory(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 2,
                 "motherboard": 10,
                 "memory": [23, 22],
                 "graphic_card": 30
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{'Placa nao suporta o tamanho total das memorias'}) 

    def test_verify_processor(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": [2,3],
                 "motherboard": 10,
                 "memory": [22],
                 "graphic_card": 30
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{'Possivel selecionar somente um processador'})

    def test_verify_motherboard(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 2,
                 "motherboard": [10,11],
                 "memory": [22],
                 "graphic_card": 30
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{'Possivel selecionar somente uma placa-mae'})

    def test_verify_memory(self):

        call_command("loaddata", "data.json", verbosity=0)
        url = ('http://127.0.0.1:8000/pcbuilder/')
        data = {
                 "client": "Teste",
                 "processor": 2,
                 "motherboard": 10,
                 "memory": [],
                 "graphic_card": 30
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,{'Selecionar pelo menos uma memória'})

        

