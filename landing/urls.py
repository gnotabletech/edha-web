from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^charcha-serviceworker(.*.js)$', views.serviceworker, name='serviceworker'),
    path('home', views.index, name='home'),
]

