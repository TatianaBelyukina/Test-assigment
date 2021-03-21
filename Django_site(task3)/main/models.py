from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    seo_title = models.CharField(max_length=150, null=True, blank=True)
    seo_description = models.CharField(max_length=150, null=True, blank=True)
    #date_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
