from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from main.models import SupplierNetwork, Product
from main.serializers import SupplierNetworkSerializer, ProductSerializer
from users.permissions import IsActive


class SupplierNetworkViewSet(ModelViewSet):
    """
    Представление для управления сетями поставщиков.
    Позволяет выполнять операции CRUD: создание, чтение, обновление и удаление.
    """
    queryset = SupplierNetwork.objects.all()
    serializer_class = SupplierNetworkSerializer
    permission_classes = [IsActive]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['country']  # Фильтрация по полю 'country'
    ordering_fields = '__all__'  # Позволяет сортировать по всем полям
    ordering = ['created_at']  # Поле по умолчанию для сортировки


class SupplierNetworkListCreateView(ListCreateAPIView):
    """
    Представление для получения списка сетей поставщиков и создания новой сети.
    """
    queryset = SupplierNetwork.objects.all()
    serializer_class = SupplierNetworkSerializer
    permission_classes = [IsActive]


class SupplierNetworkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления конкретной сети поставщиков.
    """
    queryset = SupplierNetwork.objects.all()
    serializer_class = SupplierNetworkSerializer
    permission_classes = [IsActive]


class ProductListCreateView(ListCreateAPIView):
    """
    Представление для получения списка продуктов и создания нового продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления конкретного продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
