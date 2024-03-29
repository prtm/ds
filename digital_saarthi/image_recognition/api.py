# stdlib
import json

# core django
from django.conf import settings

# third party
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# project related
from .serializers import ImageRecognitionSerializer


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        image_recognition_serializer = ImageRecognitionSerializer(
            data=request.data)

        if image_recognition_serializer.is_valid():
            # image_recognition_serializer.save()
            file_path = str(settings.ROOT_DIR.path("demo_data.json"))
            with open(file_path, 'r'):
                return Response(json.load(), status=status.HTTP_201_CREATED)
        else:
            return Response(image_recognition_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
