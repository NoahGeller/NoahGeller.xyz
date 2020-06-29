from django.urls import path
from personal_site.feeds import BlogFeed

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.detail, name='detail'),
    path('feed/', BlogFeed()),
]
