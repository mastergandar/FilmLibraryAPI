from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins

from films import serializers
from films.models import Film


class FilmListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()

    def create(self, request, *args, **kwargs):
        request.upload_handlers.pop(0)
        return super().create(request, *args, **kwargs)


class FilmUpdateDestroy(generics.UpdateAPIView, mixins.DestroyModelMixin):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()

    def patch(self, request, *args, **kwargs):
        request.upload_handlers.pop(0)
        return super().patch(request, *args, **kwargs)


class FilmSearch(generics.RetrieveAPIView):
    serializer_class = serializers.FilmSerializer
    queryset = Film.objects.all()

    def get_object(self):
        return get_object_or_404(self.queryset, name=self.kwargs['name'])
