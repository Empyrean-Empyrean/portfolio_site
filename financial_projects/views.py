from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import FinancialProject
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FinancialProjectForm

@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_financial_project(request):
    if request.method == "POST":
        form = FinancialProjectForm(request.POST, request.FILES)
        if form.is_valid():
            fp = form.save()
            form.save_m2m()
            return redirect('financial_projects:financial_detail', slug=fp.slug)
    else:
        form = FinancialProjectForm()
    return render(request, 'financial_projects/upload_financial_project.html', {'form': form})

def financial_list(request):
    search_query = request.GET.get('search', '')
    tech_filter = request.GET.get('tech', '')

    financials = FinancialProject.objects.all()
    if search_query:
        financials = financials.filter(name__icontains=search_query)
    if tech_filter:
        financials = financials.filter(technologies__name__icontains=tech_filter).distinct()

    paginator = Paginator(financials, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'tech_filter': tech_filter
    }
    return render(request, 'financial_projects/financial_list.html', context)

def financial_detail(request, slug):
    financial_project = get_object_or_404(FinancialProject, slug=slug)
    context = { 'financial_project': financial_project }
    return render(request, 'financial_projects/financial_detail.html', context)
