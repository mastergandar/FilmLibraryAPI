from rest_framework import serializers

from films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    file = serializers.FileField(read_only=True)

    class Meta:
        model = Film
        fields = [
            'pk',
            'provider',
            'name',
            'category',
            'country',
            'description',
            'actor',
            'file',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'pk',
            'file',
            'created_at',
            'updated_at',
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['file'] = 'http://127.0.0.1:8000/films' + instance.image.url
        except ValueError:
            rep['file'] = None
        return rep
