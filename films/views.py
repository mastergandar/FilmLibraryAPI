from rest_framework import generics

from films import serializers
from films.models import Film


class FilmListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()


class FilmRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()
