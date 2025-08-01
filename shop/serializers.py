from rest_framework import serializers
from .models import User,Product
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            is_admin=validated_data.get('is_admin', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock_quantity']

from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'total_price', 'created_at']


    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        total_price = 0
        order_items = []

        for item in items_data:
            product = item['product']
            quantity = item['quantity']

            if product.stock_quantity < quantity:
                raise serializers.ValidationError(f"Not enough stock for {product.name}")

            product.stock_quantity -= quantity
            product.save()

            price = product.price * quantity
            total_price += price

            order_items.append({'product': product, 'quantity': quantity})

        order = Order.objects.create(user=user, total_price=total_price)

        for item in order_items:
            OrderItem.objects.create(order=order, **item)

        return order
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']

class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderHistorySerializer(serializers.ModelSerializer):
    items = OrderItemDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'total_price', 'created_at']
