from operator import ge
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *



class WarehouseListAPIView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer 


class WarehouseCreateAPIView(generics.CreateAPIView):
    queryset = Warehouse
    serializer_class = WarehouseSerializer


class WarehouseUpdateAPIView(generics.UpdateAPIView):
    queryset = Warehouse
    serializer_class = WarehouseSerializer


class WarehouseDestroyAPIView(generics.DestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseSuperAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse
    serializer_class = WarehouseSerializer



# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product
#     serializer_class = ProductSerializer


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product
#     serializer_class = ProductSerializer


# class ProductDestroyAPIView(generics.DestroyAPIView):
#     queryset = Product
#     serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer