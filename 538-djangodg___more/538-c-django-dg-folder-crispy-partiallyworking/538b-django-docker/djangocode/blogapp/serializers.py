from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = [
            "created",
            "name",
            "author",
            "last_updated",
        ]

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = [
            "body",
            "last_updated",
            "created",
            "title",
        ]
