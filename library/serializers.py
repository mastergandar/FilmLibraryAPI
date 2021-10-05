from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from films.models import Film
from films.serializers import FilmSerializer
from library.exceptions import NotFound
from library.models import Library, LibraryProducts
from utils.helper import get_content_object, get_content_type


class LibrarySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = [
            'pk',
            'user',
            'products_count',
        ]
        read_only_fields = [
            'pk',
            'user',
            'products_count',
        ]

    @staticmethod
    def get_products_count(obj):
        return LibraryProducts.objects.filter(library=obj).count()


class LibraryProductsSerializer(serializers.ModelSerializer):
    film = FilmSerializer()

    class Meta:
        model = LibraryProducts
        fields = [
            'library',
            'film',
        ]
        read_only_fields = [
            'library',
            'film',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        content_pk = self.context["view"].kwargs['content_pk']
        library_pk = self.context["view"].kwargs['pk']
        library = Library.objects.get(pk=library_pk)
        try:
            content_object = Film.objects.get(pk=content_pk)
        except ValueError as e:
            raise NotFound(e)
        attrs["library"] = library
        attrs["content_object"] = content_object
        return attrs

    def create(self, validated_data):
        library = validated_data.pop('library')
        content_object = validated_data.pop('content_object')
        return LibraryProducts.objects.create(film=content_object, library=library)
