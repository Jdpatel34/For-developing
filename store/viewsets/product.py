from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import *
from store.serializers.products import ProductsSerializer
from store.models import Products


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

