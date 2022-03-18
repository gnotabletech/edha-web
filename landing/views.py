from django.http import HttpResponse
from django.shortcuts import render

from edharulesandbiz import settings


def service_worker(request):
    response = HttpResponse(open(settings.PWA_SERVICE_WORKER_PATH).read(), content_type='application/javascript')
    return response


def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(settings, setting_name)
        for setting_name in dir(settings)
        if setting_name.startswith('PWA_')
    }, content_type='application/json')


def offline(request):
    return render(request, "offline.html")


# Create your views here.
def index(request):
    return render(request, 'home.html')


def appstart(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


def error_403(request, exception):
    return render(request, '403_csrf.html')
