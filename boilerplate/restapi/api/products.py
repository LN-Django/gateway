from restapi.models import Product
from rest_framework import viewsets, permissions
from restapi.serializers import ProductSerializer

# ViewSet -> Create full CRUD API without declaring functionality explicitly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
