from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    main_technology = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology, related_name='projects')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    # Detailed fields
    explanation = models.TextField(blank=True, null=True)
    code_snippet = models.TextField(blank=True, null=True)
    other_info = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.slug])
    
    @property
    def content_type(self):
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(self)
