from rest_framework import generics
from .models import Task, Category, Tag
from .serializers import (TaskListSerializer,
                           TaskDetailSerializer, 
                           CategorySerializer, 
                           TagSerializer)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskDetailSerializer
        return TaskListSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'