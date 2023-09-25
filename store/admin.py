from django.contrib import admin

from store.models import Product


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


admin.site.register(Product, ProductAdmin)
