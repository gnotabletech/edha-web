from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    re_path(r'^serviceworker\.js$', views.service_worker, name='serviceworker'),
    re_path(r'^manifest\.json$', views.manifest, name='manifest'),
    re_path('^offline/$', views.offline, name='offline')
]

