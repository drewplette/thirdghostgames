from django.shortcuts import render
from django.http import HttpResponse


def splash(request):
    return render(request, 'splash.html')

def home(request):
    # Load the home page template
    return render(request, 'home.html')

def about(request):
    # Load the about page template
    return render(request, 'about.html')

def contact(request):
    # Load the contact page template
    return render(request, 'contact.html')

def crytids(request):
    # Load the cryptids page template
    return render(request, 'crytids.html')

def games(request):
    # Load the games page template
    return render(request, 'games.html')

def blog(request):
    # Load the blog page template
    return render(request, 'blog.html')





