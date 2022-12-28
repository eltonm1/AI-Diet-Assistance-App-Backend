from .models import FoodProducts, ProductPrice, NutritionInformation
from user_manager.models import User
from rest_framework import serializers
import user_manager.serializer as user_serializer
from collections import OrderedDict


class NutritionInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionInformation
        fields = '__all__'

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['price', 'supermarket', 'date']

class FoodProductsSerializer(serializers.ModelSerializer):
    product_price = ProductPriceSerializer(many=True)
    nutrition = NutritionInformationSerializer()
    created = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")
    class Meta:
        model = FoodProducts
        fields = ['id', 
                    'name', 
                    'barcode',
                    'created',
                    'manufacturer',
                    'brand',
                    'product_price',
                    'nutrition',
                 ]

    def to_representation(self, instance):
        result = super(FoodProductsSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])