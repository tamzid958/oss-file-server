from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets

from file_management.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True}
        }


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
