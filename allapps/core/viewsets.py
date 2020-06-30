from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from django.contrib.auth.models import User


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     return User.objects.filter(id=self.request.user.id)
