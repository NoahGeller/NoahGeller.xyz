from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('robots.txt', views.robots, name='robots.txt'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
]
