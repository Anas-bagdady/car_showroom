from django.db import models


class Car(models.Model):

    STATUS_CHOICES = [
        ("available", "متوفرة"),
        ("sold", "مباعة"),
        ("reserved", "محجوزة"),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان السيارة"
    )

    brand = models.CharField(
        max_length=100,
        verbose_name="الماركة"
    )

    model = models.CharField(
        max_length=100,
        verbose_name="الموديل"
    )

    year = models.PositiveIntegerField(
        verbose_name="سنة الصنع"
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="السعر"
    )

    mileage = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="عدد الكيلومترات"
    )

    color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="اللون"
    )

    fuel_type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="نوع الوقود"
    )

    transmission = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="نوع الجير"
    )

    engine_size = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="حجم المحرك"
    )

    body_type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="نوع الهيكل"
    )

    seats = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="عدد المقاعد"
    )

    description = models.TextField(
        blank=True,
        verbose_name="الوصف"
    )
    video = models.FileField(
    upload_to="cars/videos/",
    blank=True,
    null=True,
    verbose_name="فيديو السيارة"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available",
        verbose_name="الحالة"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="سيارة مميزة"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="نشطة"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخر تعديل"
    )

    class Meta:
        verbose_name = "سيارة"
        verbose_name_plural = "السيارات"

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"


class CarImage(models.Model):

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="السيارة"
    )

    image = models.ImageField(
        upload_to="cars/",
        verbose_name="الصورة"
    )

    is_main = models.BooleanField(
        default=False,
        verbose_name="الصورة الرئيسية"
    )

    class Meta:
        verbose_name = "صورة سيارة"
        verbose_name_plural = "صور السيارات"

    def __str__(self):
        return self.car.title




class SocialLink(models.Model):

    PLATFORM_CHOICES = [
        ("facebook", "فيسبوك"),
        ("instagram", "إنستغرام"),
        ("whatsapp", "واتساب"),
        ("telegram", "تلغرام"),
        ("tiktok", "تيك توك"),
        ("website", "موقع إلكتروني"),
    ]

    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES,
        verbose_name="المنصة"
    )

    url = models.URLField(
        verbose_name="الرابط"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "رابط تواصل"
        verbose_name_plural = "روابط التواصل"

    def __str__(self):
        return self.platform


class OfficeInfo(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name="اسم المكتب"
    )

    phone = models.CharField(
        max_length=30,
        verbose_name="رقم الهاتف"
    )

    whatsapp = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="رقم الواتساب"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="البريد الإلكتروني"
    )

    address = models.TextField(
        blank=True,
        verbose_name="العنوان"
    )

    description = models.TextField(
        blank=True,
        verbose_name="الوصف"
    )

    class Meta:
        verbose_name = "معلومات المكتب"
        verbose_name_plural = "معلومات المكتب"

    def __str__(self):
        return self.name