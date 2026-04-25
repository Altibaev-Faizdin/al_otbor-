from django.urls import path
from .views import (TaskListCreateView,
                     TaskDetailView, 
                     CategoryListCreateView, 
                     TagListCreateView)


urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:id>/', TaskDetailView.as_view()),
    path('categories/', CategoryListCreateView.as_view()),
    path('tags/', TagListCreateView.as_view()),
]