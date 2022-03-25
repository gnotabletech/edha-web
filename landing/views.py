import os

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from edharulesandbiz import settings
from landing.models import MemberInfo


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
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/profile')

    members = []
    for x in range(8):
        members.append(MemberInfo.objects.all().order_by('position_key')[x*3:(x+1)*3])

    return render(request, 'home.html', {'members': members, 'images': img_list})


def appstart(request):
    return render(request, 'index.html')


def portfolio(request, constituency):
    member = MemberInfo.objects.get(constituency=constituency)
    if member.othernames is None:
        member.othernames = ''
    return render(request, 'portfolio.html', {'member': member})


def member_area(request):
    if request.user.is_authenticated:
        user = request.user
        member = MemberInfo.objects.get(username=user.username)
        if member.othernames is None:
            member.othernames = ''
        return render(request, 'member_area.html', {'member': member})

    else:
        return redirect('login')


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
