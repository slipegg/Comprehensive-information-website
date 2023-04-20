from django.shortcuts import render
from rest_framework import generics
import json
from rest_framework import permissions
from .models import Weibo_hot,Weibo_hot_item,up_list,dynasic,follow_list
from .serializers import Weibo_hot_Serializer,Weibo_hot_item_Serializer,Weibo_dynasic_Serializer,Weibo_up_list_Serializer,Weibo_follow_list_Serializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.http import QueryDict
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class Weibo_hot_view(generics.ListAPIView):
    queryset = Weibo_hot.objects.all()
    serializer_class = Weibo_hot_Serializer

class Weibo_hot_item_view(generics.ListAPIView):
    queryset = Weibo_hot_item.objects.all()
    serializer_class = Weibo_hot_item_Serializer
    def get(self, request, *args, **kwargs):
        q = Weibo_hot.objects.order_by('-Weibo_hot_list_id')[0].Weibo_hot_list_id
        queryset = self.queryset.filter(Weibo_hot_list_id=q)
        while len(queryset)==0:
            q-=1
            queryset = self.queryset.filter(Weibo_hot_list_id=q)
        return Response(self.serializer_class(queryset, many=True).data)
    


class Weibo_up_list_view(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = up_list.objects.all()
    serializer_class = Weibo_up_list_Serializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        Weibo_up_name=request.data.get('Weibo_up_name')
        Weibo_up_id=request.data.get('Weibo_up_id')
        Weibo_up_face_url=request.data.get('Weibo_up_face_url')
        if up_list.objects.filter(Weibo_up_id=Weibo_up_id).exists():
            resp = {
                'status':False,
                'data':'该博主已存在'
            }
            # return Response(None)
            return Response(resp)
        else:
            up_list.objects.create(Weibo_up_id=Weibo_up_id,Weibo_up_name=Weibo_up_name,Weibo_up_face_url=Weibo_up_face_url)
            resp = {
                'status':True,
                'data':'创建成功'
            }
            return Response(resp)
    def delete(self, request, *args, **kwargs):
        DELETE = QueryDict(request.body)
        data_id=list(DELETE.keys())[0]
        dic=json.loads(data_id)
        del_id=dic["Weibo_up_id"]
        m=up_list.objects.get(Weibo_up_id=del_id)
        m.delete()
        resp = {
            'status': True,
            'data': '删除成功'
        }
        return Response(resp)

class Weibo_dynasic_view(generics.ListAPIView):
    queryset = dynasic.objects.all()
    serializer_class = Weibo_dynasic_Serializer
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticated,)  # IsAuthenticatedOrReadOnly
    def get(self, request, *args, **kwargs):
        user_id=User.objects.get(username=self.request.user).id
        follow_up=follow_list.objects.filter(Weibo_user_id=user_id)
        allup_id=[]
        for fup in follow_up:
            up_id=fup.Weibo_up_id.Weibo_up_id
            allup_id.append(up_id)
        alldyna=dynasic.objects.filter(Weibo_up_id__in=allup_id).order_by('-Weibo_post_time')[:20]
        return Response(Weibo_dynasic_Serializer(alldyna, many=True).data)

class Weibo_follow_view(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = follow_list.objects.all()
    serializer_class = Weibo_follow_list_Serializer
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticated,)  # IsAuthenticatedOrReadOnly
    def get(self, request, *args, **kwargs):
        user_id=User.objects.get(username=self.request.user).id
        follow_up=follow_list.objects.filter(Weibo_user_id=user_id)
        return Response(Weibo_follow_list_Serializer(follow_up, many=True).data)
    def post(self, request, *args, **kwargs):
        Weibo_user_id=User.objects.get(username=self.request.user)#.id
        Weibo_is_special = request.data.get('Weibo_is_special')
        Weibo_follow_name = request.data.get('Weibo_follow_name')
        Weibo_up_id = up_list.objects.filter(Weibo_up_name=Weibo_follow_name)#.Weibo_up_face_url
        Bid=0
        for b in Weibo_up_id:
            Bid=b
        follow_list.objects.create(Weibo_up_id=Bid,Weibo_user_id=Weibo_user_id,Weibo_is_special=Weibo_is_special)
        resp = {
            'status': False,
            'data': 'ok'
        }
        return Response(resp)
    def delete(self, request, *args, **kwargs):
        Weibo_user_id=User.objects.get(username=self.request.user)
        print('delete')
        DELETE = QueryDict(request.body)
        print(DELETE)
        follow_name=list(DELETE.keys())[0]
        # dic=json.loads(data_id)
        print(follow_name)
        # del_id=dic["Weibo_up_id"]
        Weibo_up = up_list.objects.get(Weibo_up_name=follow_name)
        m=follow_list.objects.get(Weibo_up_id=Weibo_up,Weibo_user_id=Weibo_user_id)
        m.delete()
        resp = {
            'status': True,
            'data': '删除成功'
        }
        return Response(resp)