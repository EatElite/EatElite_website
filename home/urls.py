from django.urls import path
from .views import home, profile_page

from django.http import HttpResponse

def okay(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('profile_page/', profile_page, name='profile_page'),    
    path('favicon.ico', okay)
    ]