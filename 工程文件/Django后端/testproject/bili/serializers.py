from rest_framework import serializers
from .models import Bili_hot,Bili_hot_item,dynasic,up_list,follow_list
from django.contrib.auth import get_user_model

class Bili_hot_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bili_hot
        fields = '__all__'

class Bili_hot_item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bili_hot_item
        fields = '__all__'#('Z_item_rank','Z_item_name','Z_item_hot','Z_item_cover_url','Z_item_url')
class Bili_up_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = up_list
        fields = '__all__'


class Bili_dynasic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = dynasic
        depth=1
        Bili_pic_urls = serializers.JSONField()#serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
        fields = '__all__'

class Bili_follow_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = follow_list
        fields = '__all__'
        depth=1