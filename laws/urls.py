from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.laws_repo, name='laws'),
    path('getlaw', views.getlaw, name='getlaw'),
    path('display_law/<value>', views.display_law, name='display_law')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

