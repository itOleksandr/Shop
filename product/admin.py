from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductCategoryGenderAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductCategoryGender


admin.site.register(ProductCategoryGender, ProductCategoryGenderAdmin)


class ProductImageForSliderAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductImageForSlider


admin.site.register(ProductImageForSlider, ProductImageForSliderAdmin)


class ProductDynamicDetailSizeAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductDynamicDetailSize


admin.site.register(ProductDynamicDetailSize, ProductDynamicDetailSizeAdmin)