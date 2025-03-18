from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),  # For Google and other auth
    path('projects/', include('projects.urls')),
    path('financial-projects/', include('financial_projects.urls')),
    path('blogs/', include('blogs.urls')),
    path('comments/', include('comments.urls')),
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
