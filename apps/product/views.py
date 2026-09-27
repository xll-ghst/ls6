from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product
from .serializers import ProductSerializer


class ProductApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    # Пагинация
    pagination_class = __import__('apps.mixin.pagination', fromlist=['HumanPag']).HumanPag

    # Фильтрация + поиск + сортировка
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'in_have', 'discount']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title', 'price', 'discount']
    ordering = ['id']

    # GET открыт, POST только авторизованным
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PoductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Для просмотра можно без авторизации, для изменения нужна авторизация
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
