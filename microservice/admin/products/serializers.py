from rest_framework import serializers

from .models import Prodcut

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodcut
        fields = '__all__'