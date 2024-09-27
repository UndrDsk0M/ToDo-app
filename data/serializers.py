from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['name']

    def create(self, validated_data):
        user = self.context['request'].user  # Get the user from the request context
        todo = Todo.objects.create(user=user, **validated_data)
        return todo