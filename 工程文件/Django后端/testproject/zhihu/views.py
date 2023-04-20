from rest_framework import generics
from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
from .models import Z_hot,Z_hot_item
from .serializers import Z_hot_Serializer,Z_hot_item_Serializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class Z_hot_view(generics.ListAPIView):
    queryset = Z_hot.objects.all()
    serializer_class = Z_hot_Serializer

class Z_hot_item_view(generics.ListAPIView):
    queryset = Z_hot_item.objects.all()
    serializer_class = Z_hot_item_Serializer

    def get(self, request, *args, **kwargs):
        q = Z_hot.objects.order_by('-Z_hot_list_id')[0].Z_hot_list_id
        queryset = self.queryset.filter(Z_hot_list_id=q)
        while len(queryset)==0:
            q-=1
            queryset = self.queryset.filter(Z_hot_list_id=q)
        return Response(self.serializer_class(queryset, many=True).data)
