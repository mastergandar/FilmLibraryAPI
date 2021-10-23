from rest_framework import serializers

from films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=True)

    class Meta:
        model = Film
        fields = [
            'pk',
            'provider',
            'film_id',
            'name',
            'category',
            'country',
            'description',
            'image',
            'actor',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'pk',
            'created_at',
            'updated_at',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['image'] = 'http://127.0.0.1:8000/films' + instance.image.url
        except ValueError:
            rep['image'] = None
        return rep
