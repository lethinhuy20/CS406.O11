from rest_framework import serializers

class ImageFeaturesSerializer(serializers.Serializer):
    """Serializes image features and metadata."""
    id = serializers.IntegerField()
    features = serializers.ListField(child=serializers.FloatField())
    metadata = serializers.JSONField()