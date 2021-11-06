from rest_framework import serializers
# from talk.models import Post


class PostSerializer(serializers.Serializer):

    username = serializers.CharField()

class VideoSerializer(serializers.Serializer):

    userid = serializers.CharField()
    counts = serializers.CharField()

