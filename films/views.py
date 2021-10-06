from rest_framework import generics

from films import serializers
from films.models import Film


class FilmListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()

    def create(self, request, *args, **kwargs):
        request.upload_handlers.pop(0)
        return super().create(request, *args, **kwargs)


class FilmRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()

    def patch(self, request, *args, **kwargs):
        request.upload_handlers.pop(0)
        return super().patch(request, *args, **kwargs)
