from django.shortcuts import render
from rest_framework import generics
import json
from rest_framework import permissions
from .models import Bili_hot,Bili_hot_item,up_list,dynasic,follow_list
from .serializers import Bili_hot_Serializer,Bili_hot_item_Serializer,Bili_dynasic_Serializer,Bili_up_list_Serializer,Bili_follow_list_Serializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.http import QueryDict
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class Bili_hot_view(generics.ListAPIView):
    queryset = Bili_hot.objects.all()
    serializer_class = Bili_hot_Serializer

class Bili_hot_item_view(generics.ListAPIView):
    queryset = Bili_hot_item.objects.all()
    serializer_class = Bili_hot_item_Serializer
    def get(self, request, *args, **kwargs):
        q = Bili_hot.objects.order_by('-Bili_hot_list_id')[0].Bili_hot_list_id
        queryset = self.queryset.filter(Bili_hot_list_id=q)
        while len(queryset)==0:
            q-=1
            queryset = self.queryset.filter(Bili_hot_list_id=q)
        return Response(self.serializer_class(queryset, many=True).data)

class Bili_up_list_view(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = up_list.objects.all()

    authentication_classes = []
    serializer_class = Bili_up_list_Serializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        Bili_up_name=request.data.get('Bili_up_name')
        Bili_up_id=request.data.get('Bili_up_id')
        Bili_up_face_url=request.data.get('Bili_up_face_url')
        if up_list.objects.filter(Bili_up_id=Bili_up_id).exists():
            resp = {
                'status':False,
                'data':'该up主已存在'
            }
            return Response(resp)
        else:
            up_list.objects.create(Bili_up_id=Bili_up_id,Bili_up_name=Bili_up_name,Bili_up_face_url=Bili_up_face_url)
            resp = {
                'status':True,
                'data':'创建成功'
            }
            return Response(resp)
    def delete(self, request, *args, **kwargs):
        print('delete')
        DELETE = QueryDict(request.body)
        data_id=list(DELETE.keys())[0]
        dic=json.loads(data_id)
        del_id=dic["Bili_up_id"]
        m=up_list.objects.get(Bili_up_id=del_id)
        m.delete()
        resp = {
            'status': True,
            'data': '删除成功'
        }
        return Response(resp)

class Bili_dynasic_view(generics.ListAPIView):
    queryset = dynasic.objects.all()
    serializer_class = Bili_dynasic_Serializer
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticated,)  # IsAuthenticatedOrReadOnly
    def get(self, request, *args, **kwargs):
        print(self.request.user)
        user_id=User.objects.get(username=self.request.user).id
        follow_up=follow_list.objects.filter(Bili_user_id=user_id)
        allup_id=[]
        for fup in follow_up:
            up_id=fup.Bili_up_id.Bili_up_id
            allup_id.append(up_id)
        alldyna=dynasic.objects.filter(Bili_up_id__in=allup_id).order_by('-Bili_post_time')
        return Response(Bili_dynasic_Serializer(alldyna, many=True).data)

class Bili_follow_view(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = follow_list.objects.all()
    serializer_class = Bili_follow_list_Serializer
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticated,)  # IsAuthenticatedOrReadOnly
    def get(self, request, *args, **kwargs):
        user_id=User.objects.get(username=self.request.user).id
        follow_up=follow_list.objects.filter(Bili_user_id=user_id)
        return Response(Bili_follow_list_Serializer(follow_up, many=True).data)

    def post(self, request, *args, **kwargs):
        Bili_user_id=User.objects.get(username=self.request.user)#.id
        Bili_is_special = request.data.get('Bili_is_special')
        Bili_follow_name = request.data.get('Bili_follow_name')
        Bili_up_id = up_list.objects.filter(Bili_up_name=Bili_follow_name)#.Bili_up_face_url
        Bid=0
        for b in Bili_up_id:
            Bid=b
            print("Bili_up_id",b)
        follow_list.objects.create(Bili_up_id=Bid,Bili_user_id=Bili_user_id,Bili_is_special=Bili_is_special)
        resp = {
            'status': False,
            'data': 'ok'
        }
        return Response(resp)
    def delete(self, request, *args, **kwargs):
        Bili_user_id=User.objects.get(username=self.request.user)
        DELETE = QueryDict(request.body)
        follow_name=list(DELETE.keys())[0]
        Bili_up = up_list.objects.get(Bili_up_name=follow_name)
        m=follow_list.objects.get(Bili_up_id=Bili_up,Bili_user_id=Bili_user_id)
        m.delete()
        resp = {
            'status': True,
            'data': '删除成功'
        }
        return Response(resp)
