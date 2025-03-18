from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from blogs.models import Blog
from django.contrib.auth.decorators import login_required, user_passes_test

def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def dashboard_view(request):
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'dashboard/dashboard.html', {'projects': projects, 'blogs': blogs})

@login_required
@user_passes_test(superuser_required)
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('dashboard:dashboard')

@login_required
@user_passes_test(superuser_required)
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('dashboard:dashboard')
