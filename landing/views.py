from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def serviceworker(request, js):
    template = get_template('serviceworker.js')
    html = template.render()
    return HttpResponse(html, content_type="application/x-javascript")


# Create your views here.
def index(request):
    return render(request, 'index.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')