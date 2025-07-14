from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),  # Make splash the root URL
    path('home/', views.home, name='home'),  # Move home to /home/
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('games/', views.games, name='games'),
    path('blog/', views.blog, name='blog'),
    path('cryptids/', views.crytids, name='cryptids'),
]
