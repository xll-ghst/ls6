from django.core.cache import cache
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Task
from .serializers import TaskSerializer


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    # Пагинация
    pagination_class = __import__('apps.mixin.pagination', fromlist=['HumanPag']).HumanPag

    # Фильтрация + поиск + сортировка
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title']
    ordering = ['id']

    # GET открыт, POST только авторизованным
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
        # После создания нового объекта очищаем старый кэш.
        cache.delete('tasks')
