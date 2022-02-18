from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about', views.about, name='about'),
]