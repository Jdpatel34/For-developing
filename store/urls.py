from django.urls import include, path
from rest_framework import routers
from store.viewsets.user import LoginUserViewSet, UserViewSet
from store.viewsets.product import ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'login', LoginUserViewSet)
router.register(r'products', ProductsViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('users/', UserViewSet.as_view(), name='users'),
#     path('login/', LoginUserViewSet.as_view(), name='login'),
#     path('products/', ProductsViewSet.as_view(), name='products'),
# ]
