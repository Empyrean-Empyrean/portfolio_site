from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()  # Could be markdown or HTML content
    excerpt = models.CharField(max_length=300, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', args=[self.slug])
    
    @property
    def content_type(self):
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(self)
