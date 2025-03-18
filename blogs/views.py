from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blog
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BlogForm

def blog_list(request):
    search_query = request.GET.get('search', '')
    blogs = Blog.objects.all()
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)

    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'blogs/blog_list.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = { 'blog': blog }
    return render(request, 'blogs/blog_detail.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_list')
    else:
        form = BlogForm()
    return render(request, 'blogs/upload_blog.html', {'form': form})