from django.shortcuts import render


from rest_framework import viewsets
from User.serializers import UserSerializer
from User.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer