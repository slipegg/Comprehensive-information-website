from rest_framework import serializers
from .models import Weibo_hot,Weibo_hot_item,up_list,dynasic,follow_list
from django.contrib.auth import get_user_model

class Weibo_hot_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Weibo_hot
        fields = '__all__'

class Weibo_hot_item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Weibo_hot_item
        fields = '__all__'
class Weibo_up_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = up_list
        fields = '__all__'

class Weibo_dynasic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = dynasic
        depth=1
        Weibo_pic_urls = serializers.JSONField()#serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
        fields = '__all__'

class Weibo_follow_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = follow_list
        fields = '__all__'
        depth=1