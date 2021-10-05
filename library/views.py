from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from library import serializers
from library.models import Library, LibraryProducts


class LibraryListView(generics.ListAPIView):
    serializer_class = serializers.LibrarySerializer
    queryset = Library.objects.all()


class LibraryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LibrarySerializer
    queryset = Library.objects.all()


class LibraryProductsListView(generics.ListAPIView):
    serializer_class = serializers.LibraryProductsSerializer
    queryset = LibraryProducts.objects.all()


class LibraryProductsRetrieveUpdateDestroy(generics.GenericAPIView,
                                           mixins.CreateModelMixin,
                                           mixins.DestroyModelMixin):
    serializer_class = serializers.LibraryProductsSerializer
    queryset = LibraryProducts.objects.all()

    def get_object(self):
        return get_object_or_404(self.queryset, film_id=self.kwargs["content_pk"])

    def post(self, request, *args, **kwargs):
        """ Create new like to specified content """
        return super().create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
