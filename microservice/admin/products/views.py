from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer

import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # route: /api/products
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
        
    def create(self, request): # route: /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
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
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None): # route: /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(data=HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })