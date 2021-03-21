from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('title', 'slug', 'seo_title', 'seo_description', 'body')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Post, PostAdmin)  # Use the customized options