from rest_framework import serializers
from .models import Task, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed', 'created_at']


class TaskDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    tags_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'created_at',
                  'category', 'tags', 'category_id', 'tags_ids']

    def create(self, validated_data):
        tags_ids = validated_data.pop('tags_ids', [])
        task = Task.objects.create(**validated_data)
        task.tags.set(tags_ids)
        return task

    def update(self, instance, validated_data):
        tags_ids = validated_data.pop('tags_ids', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.tags.set(tags_ids)
        return instance