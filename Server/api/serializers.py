from rest_framework import serializers
from app.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'