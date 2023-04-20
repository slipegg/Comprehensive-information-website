from django.contrib.auth.models import User
from .models import Article,crawlTimeManage
from rest_framework.authtoken.views import APIView,AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer,crawlTimeManageSerializer
# 用户注册
class Register(APIView):
    authentication_classes = []
    def post(self,request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print('username,password:',username,password)
        try:
            is_staff=request.data.get("is_staff")
            if not is_staff:
                is_staff = "False"
        except:
            is_staff="False"
        if User.objects.filter(username=username).exists():
            resp = {
                'status':False,
                'data':'用户名已被注册'
            }
        else:
            user = User.objects.create_user(username=username,password=password,is_staff=is_staff)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                'status':True,
                'token': token.key,
                'user_id': user.pk,
                'user_name': user.username,
            }
        return Response(resp)
class ChangePasswd(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)  # token认证
    def post(self, request, *args, **kwargs):
        user=User.objects.get(username=self.request.user)
        user.set_password(request.data.get('newpassword'))
        user.save()
        return Response(status=200)

class ChangeName(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)  # token认证
    def post(self, request, *args, **kwargs):
        user=User.objects.get(username=self.request.user)
        user.username=request.data.get('newname')
        user.save()
        return Response(status=200)

class rootChangePasswd(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        print(request.data)
        user=User.objects.get(username=request.data['username'])
        user.set_password(request.data['newpassword'])
        user.save()
        return Response(status=200)


class normalUser(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        a=User.objects.all().filter(is_staff="False")
        s=UserSerializer(a,many=True)
        return Response(s.data)
    def post(self, request, *args, **kwargs):
        m=User.objects.get(username=request.data['data']['username'])
        m.delete()
        resp = {
            'status': True,
            'data': '删除成功'
        }
        return Response(resp)
class superUser(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        a=User.objects.all().filter(is_staff="True")
        s=UserSerializer(a,many=True)
        return Response(s.data)
    def post(self, request, *args, **kwargs):
        print(request.data)
        m=User.objects.get(username=request.data['data']['username'])
        m.delete()
        resp = {
            'status': True,
            'data': '删除成功'
        }
        return Response(resp)
class isRoot(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticated,)  # IsAuthenticatedOrReadOnly
    def get(self, request, *args, **kwargs):
        res=User.objects.filter(username=self.request.user)
        resp = {
            'status': res[0].is_staff,
        }
        return Response(resp)
# 用户登录
class Login(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        a=User.objects.all()
        s=UserSerializer(a,many=True)
        return Response(s.data)
    def post(self, request, *args, **kwargs):
        print("request.data:",request.data)
        serializer = AuthTokenSerializer(data=request.data,context={'request': request})
        if not serializer.is_valid():
            return Response({
            'status':403,
            'data':"用户名或密码不正确",
        })
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'status':200,
            'token': token.key,
            'user_id': user.pk,
            'user_name':user.username,
        })
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.authentication import TokenAuthentication

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticated,)#IsAuthenticatedOrReadOnly
    # important
    def get(self, request, *args, **kwargs):
        print('==================')
        print(self.request.user)
        print('==================')
        print(request.data)
        return Response(ArticleSerializer(Article.objects.get(pk=3)).data)
        # return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        print('==================')
        print(self.request.user)
        print('==================')
        serializer.save()#(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class =ArticleSerializer
    authentication_classes = (TokenAuthentication,)  # token认证
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class crawlTimeManageList(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        a=crawlTimeManage.objects.filter(pk=1)[0]
        print(a)
        s=crawlTimeManageSerializer(a)
        return Response(s.data)
    def post(self, request, *args, **kwargs):
        print(request.data)
        flag=True
        if not (str(request.data['biliDynasicTime']).isdigit() and str(request.data['weiboDynasicTime']).isdigit()
        and str(request.data['biliHotTime']).isdigit()and str(request.data['weiboHotTime']).isdigit()
        and str(request.data['zhihuHotTime']).isdigit()):
            flag=False
        if flag:
            a = crawlTimeManage.objects.filter(pk=1)[0]
            a.biliDynasicTime = request.data['biliDynasicTime']
            a.weiboDynasicTime = request.data['weiboDynasicTime']
            a.biliHotTime = request.data['biliHotTime']
            a.weiboHotTime = request.data['weiboHotTime']
            a.zhihuHotTime = request.data['zhihuHotTime']
            a.save()
            resp = {
                'status': True,
                'data': '修改成功'
            }
        else:
            resp = {
                'status': False,
                'data': '数据错误'
            }
        return Response(resp)
