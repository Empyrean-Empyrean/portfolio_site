from django.urls import path
from .views import dashboard_view, delete_project, delete_blog

app_name = "dashboard"  # Add this to avoid namespace errors

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("delete/project/<int:pk>/", delete_project, name="delete_project"),
    path("delete/blog/<int:pk>/", delete_blog, name="delete_blog"),
]
