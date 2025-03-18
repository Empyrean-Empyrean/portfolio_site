from django.db import models
from django.urls import reverse
from projects.models import Technology

class FinancialProject(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    main_technology = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology, related_name='financial_projects')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    explanation = models.TextField(blank=True, null=True)
    code_snippet = models.TextField(blank=True, null=True)
    other_info = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('financial_projects:financial_detail', args=[self.slug])
    
    @property
    def content_type(self):
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(self)
