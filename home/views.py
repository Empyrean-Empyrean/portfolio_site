from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'Home',
        'welcome_message': "Hi, I'm Sridhar Somisetti, a Data Scientist and Django Developer."
    }
    return render(request, 'home/index.html', context)
