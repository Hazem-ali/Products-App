from rest_framework import serializers
from rest_framework.utils import field_mapping

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name','email', 'password') # NOTE show fields 
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # NOTE override django create for this serializer
    def create(self, validated_data):
        """create and return user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user




# class OrderSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.Order
#         fields = ('id', 'user') # NOTE show fields 


class ProductSerializer(serializers.ModelSerializer):
    """Serialize object"""

    class Meta:
        model = models.Product
        fields = ('id', 'name','price','inventory') # NOTE show fields 
class OrderSerializer(serializers.ModelSerializer):
    """Serialize object"""

    class Meta:
        model = models.Order
        fields = ('product','quantity') # NOTE show fields 


class CartSerializer(serializers.ModelSerializer):
    """Serialize object"""

    class Meta:
        model = models.Cart
        fields = '__all__'
