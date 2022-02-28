from django.urls import path

from . import views

urlpatterns = [
    path('', views.laws_repo, name='laws'),
    path('getlaw', views.getlaw, name='getlaw'),
    path('display_law/<value>', views.display_law, name='display_law')
]
