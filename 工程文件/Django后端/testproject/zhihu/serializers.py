from rest_framework import serializers
from .models import Z_hot,Z_hot_item
from django.contrib.auth import get_user_model
class Z_hot_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Z_hot
        fields = '__all__'

class Z_hot_item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Z_hot_item
        fields = '__all__'