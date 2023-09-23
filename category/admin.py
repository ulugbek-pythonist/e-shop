from django.contrib import admin

from category.models import Category


class CategAdmin(admin.ModelAdmin):
    list_display = ("category_name", "slug", "description")
    prepopulated_fields = {"slug": ("category_name",)}


admin.site.register(Category, CategAdmin)
