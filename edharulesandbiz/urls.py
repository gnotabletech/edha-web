"""edharulesandbiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('edharules/', include('edharules.urls')),
    path('laws/', include('laws.urls')),
    path('', include('authenticate.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'landing.views.error_404'
handler500 = 'landing.views.error_500'
handler403 = 'landing.views.error_403'

admin.site.site_header = "EDHA E-Parliament/Website Administration"
admin.site.site_title = "EDHA E-Parliament/Website Administration"
admin.site.index_title = "EDHA E-Parliament/Website Administration"