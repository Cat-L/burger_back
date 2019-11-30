from .views import OrderViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='orders', viewset=OrderViewSet, base_name='orders')

urlpatterns = [
    # path('orders/<int:pk>/')
    # path('order/', OrderList.as_view(), name='order_list'),
    # path('order/<int:pk>', OrderDetail.as_view(), name='order_detail'),
]

urlpatterns += router.urls
