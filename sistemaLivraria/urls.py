from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about', views.about, name='about'),
    path('livros', views.livros, name='livros'),
    path('livros/criar', views.criar, name='criar'),
    path('livros/editar', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('livros/editar/<int:id>', views.editar, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)