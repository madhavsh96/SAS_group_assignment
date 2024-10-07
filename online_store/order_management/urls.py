from django.urls import path, include
from rest_framework import routers

from order_management.views import CategoryViewSet, ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]