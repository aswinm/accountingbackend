from django.shortcuts import render
from clients.models import Client
from rest_framework import viewsets
from clients.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer



# Create your views here.
