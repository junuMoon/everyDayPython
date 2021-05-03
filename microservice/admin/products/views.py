from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # route: /api/products
        product = Product.objects.all()
        print(type(product))
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
        
    def create(self, request): # route: /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None): # route: /api/products/<str:id>
        product = Product.objects.filter(id=pk).values()[0]
        serializer = ProductSerializer(data=product)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
        
    
    def update(self, request, pk=None): # route: /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None): # route: /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(data=HTTP_204_NO_CONTENT)
