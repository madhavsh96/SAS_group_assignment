from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        # Deduct stock for ordered products
        for product in order.product.all():
            product.stock -= 1
            product.save()


