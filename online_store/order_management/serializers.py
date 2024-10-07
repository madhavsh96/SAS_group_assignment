from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id","name","description"]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id","name","description","price","category","stock"]

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ["id","product","total_amount","user"]
    
    def validate(self, data):

        # Check stock availability
        for product in data['product']:
            prod = Product.objects.get(id=product.id)
            if prod.stock < 1:
                raise serializers.ValidationError(f"Product {prod.name} is out of stock.")
            if data["total_amount"] != product.price:
                raise serializers.ValidationError(f"Please enter the correct total amount")
        return data
