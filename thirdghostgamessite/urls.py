from django.urls import path
from datetime import datetime
from django.utils import timezone
from . import views

def is_past_launch_date():
    # Set your launch date here
    launch_date = datetime(2025, 12, 25, 0, 0, 0)  # Year, Month, Day, Hour, Minute, Second
    
    # Make it timezone aware
    launch_date = timezone.make_aware(launch_date)
    
    # Get current date and time
    now = timezone.now()
    
    # Compare current date with launch date
    return now >= launch_date

# Base URL patterns (always available)
urlpatterns = [
    path('', views.splash, name='splash'),  # Make splash the root URL
]

# Add additional URLs if past launch date
if is_past_launch_date():
    urlpatterns.extend([
        path('home/', views.home, name='home'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('games/', views.games, name='games'),
        path('blog/', views.blog, name='blog'),
        path('cryptids/', views.cryptids, name='cryptids'),
    ])
else:
    # Before launch date, redirect all URLs back to splash
    urlpatterns.extend([
        path('home/', views.splash, name='home'),  # Same name 'home' but goes to splash
        path('about/', views.splash, name='about'),
        path('contact/', views.splash, name='contact'),
        path('games/', views.splash, name='games'),
        path('blog/', views.splash, name='blog'),
        path('cryptids/', views.splash, name='cryptids'),
    ])
