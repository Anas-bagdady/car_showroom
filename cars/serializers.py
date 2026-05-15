from rest_framework import serializers
from .models import Car, CarImage, SocialLink, OfficeInfo


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = "__all__"


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"


class OfficeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeInfo
        fields = "__all__"