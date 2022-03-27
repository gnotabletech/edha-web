from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('appstart', views.appstart, name='appstart'),
    path('route/<sender>', views.route, name='route'),
    path('news', views.news, name='news'),
    path('news_detail', views.news_detail, name='news_detail'),
    path('member_area', views.member_area, name='member_area'),
    path('portfolio/<constituency>', views.portfolio, name='portfolio'),
    re_path(r'^serviceworker\.js$', views.service_worker, name='serviceworker'),
    re_path(r'^manifest\.json$', views.manifest, name='manifest'),
    re_path('^offline/$', views.offline, name='offline')
]

