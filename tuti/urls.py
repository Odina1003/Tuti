from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
]
