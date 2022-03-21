from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

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


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('member_area')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')


# Create your views here.
def index(request):
    return render(request, 'home.html')


def appstart(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def member_area(request):
    return render(request, 'member_area.html')


def route(request, sender):
    if sender == "website":
        request.session['sender'] = "website"
        return redirect('login')
    else:
        request.session['sender'] = "app"
        return redirect('login')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


def error_403(request, exception):
    return render(request, '403_csrf.html')


def news(request):
    return render(request, 'blog.html')
