from django.urls import path
from . import views

app_name = 'financial_projects'

urlpatterns = [
    path('upload/', views.upload_financial_project, name='upload_financial_project'),
    path('<slug:slug>/', views.financial_detail, name='financial_detail'),
    path('', views.financial_list, name='financial_list'),
]
