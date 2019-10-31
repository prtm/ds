# third party
from rest_framework import serializers

# project related
from .models import ImageRecognition


class ImageRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRecognition
        fields = "__all__"
