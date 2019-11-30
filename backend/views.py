from .serializers import OrderDetailSerializer, OrderListSerializer, OrderSerializer
from .models import Order
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    去除 CSRF 检查
    """

    def enforce_csrf(self, request):
        return


# #
# class OrderList(generics.RetrieveAPIView):
#     authentication_classes = (CsrfExemptSessionAuthentication)
#
#     queryset = Order.objects.all()
#     # serializer_class = OrderListSerializer
#     serializer_class = OrderDetailSerializer
#
#
# class OrderDetail(generics.UpdateAPIView):
#     authentication_classes = (CsrfExemptSessionAuthentication)
#
#     queryset = Order.objects.all()
#     serializer_class = OrderDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
