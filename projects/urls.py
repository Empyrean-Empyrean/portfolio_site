from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('upload/', views.upload_project, name='upload_project'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('', views.project_list, name='project_list'),
]
