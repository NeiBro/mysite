from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string    

def index(request):
    return render(request, 'owner/index.html')

def contact(request):
    data = {'mail': 'nuransw@gmail.com'}
    return render(request, 'owner/contact.html', data)

def projects(request):
    projects = [
        {'id': 1, 'title': 'Проект 1', 'image_url': 'project1.jpg', 'project_url': 'https://github.com/NeiBro/logparser'},
        {'id': 2, 'title': 'Проект 2', 'image_url': 'project2.jpg', 'project_url': 'https://github.com/NeiBro/telemetrioparser'},
    ]
    return render(request, 'owner/projects.html', context={'projects': projects})

def page_not_found(request, exception):
    notfound = render_to_string('owner/pagenotfound.html', {'title': "Страница не найдена"})
    return HttpResponseNotFound(notfound)