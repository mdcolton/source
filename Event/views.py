from django.shortcuts import render

from rest_framework import viewsets
from Event.serializers import EventSerializer
from Event.models import Event


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
