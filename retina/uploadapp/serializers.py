from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'name', 'timestamp')

class ResultSerializer(serializers.Serializer):
    class Meta:
        result_details = serializers.CharField(max_length=200)