from rest_framework import serializers

from goods.models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'slug', 'name', 'price', 'quantity', 'discount', 'category', 'description']
