from django.shortcuts import render

# Create your views here.
import control.models
from . import serializers
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters


class SomeControlList(viewsets.ModelViewSet):
    queryset = control.models.SomeControl.objects.all()
    serializer_class = serializers.ControlSomeControlSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('title', 'owner')
