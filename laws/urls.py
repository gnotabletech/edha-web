from django.urls import path

from . import views

urlpatterns = [
    path('', views.laws_repo, name='laws'),
    path('laws_repo_more/<last_record>', views.laws_repo_more, name='next_laws'),
    path('getlaw', views.getlaw, name='getlaw'),
    path('print', views.print_law, name='print')
]

