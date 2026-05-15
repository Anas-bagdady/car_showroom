from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Car, SocialLink, OfficeInfo
from .serializers import CarSerializer, SocialLinkSerializer, OfficeInfoSerializer


class AdminOrReadOnlyMixin:
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]


class CarViewSet(AdminOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class SocialLinkViewSet(AdminOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = SocialLink.objects.filter(is_active=True)
    serializer_class = SocialLinkSerializer


class OfficeInfoViewSet(AdminOrReadOnlyMixin, viewsets.ModelViewSet):
    queryset = OfficeInfo.objects.all()
    serializer_class = OfficeInfoSerializer