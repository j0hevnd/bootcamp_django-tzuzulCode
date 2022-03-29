from rest_framework import serializers

from apps.ejmp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer2(serializers.Serializer):
    name_product = serializers.CharField(max_length=40)
    stock = serializers.IntegerField()
    price = serializers.FloatField()
    # description = serializers.CharField(max_length=100)

    def validate_name_product(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('nombre muy corto')
        return value
    
    def validate_stock(self, value):
        if value < 1:
            raise serializers.ValidationError('no valido')
        return value
    
    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('no valido')
        return value

    def create(self, validate_data):
        return Product.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name_product = validate_data.get('name_product')
        instance.stock = validate_data['stock']
        instance.price = validate_data.get('price')
        instance.save()
        return instance


