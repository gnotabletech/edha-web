from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('search', views.search, name='search'),
    path('counter/<value>', views.counter, name='counter'),
    path('jumptosection/<path:val>', views.jumptosection, name='jump_to_section')
]
