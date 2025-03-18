from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProjectForm

@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            form.save_m2m()  # Save many-to-many relations if any
            return redirect('projects:project_detail', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'projects/upload_project.html', {'form': form})

def project_list(request):
    search_query = request.GET.get('search', '')
    tech_filter = request.GET.get('tech', '')

    projects = Project.objects.all()
    if search_query:
        projects = projects.filter(name__icontains=search_query)
    if tech_filter:
        projects = projects.filter(technologies__name__icontains=tech_filter).distinct()

    paginator = Paginator(projects, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'tech_filter': tech_filter
    }
    return render(request, 'projects/project_list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = { 'project': project }
    return render(request, 'projects/project_detail.html', context)
