from django.shortcuts import render

def index(request):
    return render(request, 'articles.html', context={'name': 'articles',})
