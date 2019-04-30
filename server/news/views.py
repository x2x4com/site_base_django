from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from . import models


# class MyModelViewSet(ModelViewSet):
#    model = models.MyModel

class NewsViewSet(ModelViewSet):
    model = models.News
    # ordering = ['-create_time']
    list_display = ('title', 'type', 'owner', 'create_time')


class TypeViewSet(ModelViewSet):
    model = models.Type
    # ordering = ['-create_time']
    list_display = ('name',)


class NewsApiList(APIView):
    """
    List all news

    """
    @staticmethod
    def get_object(pk):
        try:
            return models.News.objects.get(pk=pk)
        except models.News.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="get all news",)
    def get(self, request):
        n = models.News.objects.all()
        s = NewsSerializer(n, many=True)
        return Response(s.data)

    def post(self, request):
        s = NewsSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = self.get_object(pk)
        s = NewsSerializer(obj, data=request.data)
