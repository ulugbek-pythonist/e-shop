from django.contrib import admin

from store.models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "stock",
        "category",
        "created_date",
        "updated_date",
    )
    prepopulated_fields = {"slug": ["title"]}


class VariationAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "variation_type",
        "variation_val",
        "is_active",
        "created_at",
    )
    list_editable = ("is_active",)
    list_filter = (
        "product",
        "variation_type",
        "variation_val",
        "is_active",
        "created_at",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
