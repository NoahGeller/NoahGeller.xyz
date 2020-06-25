from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug:slug>/', views.detail, name='detail'),
]
