from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # route: /api/products
        #TODO: make view
        pass 
    
    def create(self, request): # route: /api/products
        pass
    
    def retrieve(self, request, pk=None): # route: /api/products/<str:id>
        pass
    
    def update(self, request, pk=None): # route: /api/products/<str:id>
        pass
    
    def destroy(self, request, pk=None): # route: /api/products/<str:id>
        pass