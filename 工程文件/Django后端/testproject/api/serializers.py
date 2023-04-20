from rest_framework import serializers
from .models import Article,crawlTimeManage
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email','is_staff','date_joined')
class crawlTimeManageSerializer(serializers.ModelSerializer):
    class Meta:
        model=crawlTimeManage
        fields = '__all__'
# class UserSerializer(serializers.ModelSerializer):
#     articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'articles',)
#         read_only_fields = ('id', 'username',)

class ArticleSerializer(serializers.ModelSerializer):
    # author = UserSerializer() # required=False表示可接受匿名用户，many=True表示有多个用户。
    status = serializers.ReadOnlyField(source="get_status_display")
    # cn_status = serializers.SerializerMethodField()
    # author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id','create_date')#,'author'

    def get_cn_status(self, obj):
        if obj.status == 'p':
            return "已发表"
        elif obj.status == 'd':
            return "草稿"
        else:
            return ''
