from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('upload/', views.upload_blog, name='upload_blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('', views.blog_list, name='blog_list'),
]
