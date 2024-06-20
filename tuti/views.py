from django.shortcuts import render

def index(request):
    return render(request=request, template_name='index.html', context={})

def about(request):
    return render(request=request, template_name='about.html', context={})

def courses(request):
    return render(request=request, template_name='courses.html', context={})

def contact(request):
    return render(request=request, template_name='contact.html', context={})