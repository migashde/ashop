from django.contrib import admin
from categories.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_image', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

    def display_image(self, obj):
        return f'<img src="{obj.image.url}" width="50" height="50" />'

    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
