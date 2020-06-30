from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='todo-detail',
        read_only=True
    )

    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail'
    )
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'url', 'todos']
