from django.contrib import admin
from .models import Car, CarImage, SocialLink, OfficeInfo


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brand",
        "model",
        "year",
        "price",
        "status",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "status",
        "brand",
        "year",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "brand",
        "model",
        "color",
    )

    inlines = [CarImageInline]


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = (
        "car",
        "image",
        "is_main",
    )

    list_filter = (
        "is_main",
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "platform",
        "url",
        "is_active",
    )

    list_filter = (
        "platform",
        "is_active",
    )


@admin.register(OfficeInfo)
class OfficeInfoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "whatsapp",
        "email",
    )