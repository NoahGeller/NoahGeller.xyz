from django.shortcuts import render, get_object_or_404

from .models import Project

def index(request):
    projects = Project.objects.order_by('-name')
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)

def detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/detail.html', context)
