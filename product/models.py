from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = "Категории товаров"


class ProductCategoryGender(models.Model):
    gender_name = models.CharField(max_length=64,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.gender_name

    class Meta:
        verbose_name = 'Гендерная категория товара '
        verbose_name_plural = 'Гендерные категории товаров'


class ProductDynamicDetailSize(models.Model):
    size = models.CharField(max_length=32, blank=True, null=True, default=None)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.size, self.color)

    class Meta:
        verbose_name = 'Динамическая характеристика размера '
        verbose_name_plural = 'Динамические характеристики размера'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True, default=None)
    dynamic_detail = models.ForeignKey(ProductDynamicDetailSize, blank=True, null=True, default=None, on_delete=models.CASCADE)
    brand = models.CharField(max_length=64, blank=True, null=True, default=None)
    material = models.CharField(max_length=64, blank=True, null=True, default=None)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gender = models.ForeignKey(ProductCategoryGender, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class ProductImageForSlider(models.Model):
    description_title = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_image = models.CharField(max_length=64, blank=True, null=True, default=None)
    image_slider = models.ImageField(upload_to='slider_images/')
    is_active = models.BooleanField(default=True)
    to_placement = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фотография на слайдер'
        verbose_name_plural = 'Фотографии на слайдер'