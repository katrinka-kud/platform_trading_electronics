from django.urls import path
from rest_framework.routers import SimpleRouter

from main.apps import MainConfig
from main.views import SupplierNetworkViewSet, SupplierNetworkListCreateView, SupplierNetworkRetrieveUpdateDestroyView, \
    ProductListCreateView, ProductRetrieveUpdateDestroyView

app_name = MainConfig.name

router = SimpleRouter()
router.register('', SupplierNetworkViewSet)

urlpatterns = [
    path('suppliers/', SupplierNetworkListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierNetworkRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]

urlpatterns += router.urls
