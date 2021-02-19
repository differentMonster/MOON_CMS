from rest_framework import serializers
from cart.models import UserAccountModel, CartModel

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccountModel
        fields = '__all__'
        depth = 1

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'
