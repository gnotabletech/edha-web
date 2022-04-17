from django.urls import path

from . import views

urlpatterns = [
    path('', views.laws_repo, name='laws'),
    path('laws_repo_more/<last_record>', views.laws_repo_more, name='next_laws'),
    path('getlaw', views.getlaw, name='getlaw'),
    path('print', views.print_law, name='print'),
    path('print_report', views.print_law_report, name='print_report'),
    path('print_pending_bills', views.print_pending_bills, name='print_pending_bills'),
    path('print_assented_laws', views.print_assented_laws, name='print_assented_laws'),
    path('get_law_by_assembly', views.get_law_by_assembly, name='get_law_by_assembly')
]

