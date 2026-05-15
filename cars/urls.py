from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarViewSet, SocialLinkViewSet, OfficeInfoViewSet

router = DefaultRouter()

router.register("cars", CarViewSet, basename="cars")
router.register("social-links", SocialLinkViewSet, basename="social-links")
router.register("office-info", OfficeInfoViewSet, basename="office-info")

urlpatterns = [
    path("", include(router.urls)),
]