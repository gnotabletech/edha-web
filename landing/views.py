from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')