import os

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect

from edharulesandbiz import settings
from landing.models import MemberInfo, StaffResume, News, MemberResume
from laws.models import BillsAndLaws


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
    login_status = request.session.get('login_status')
    members = []
    for x in range(8):
        members.append(MemberInfo.objects.all().order_by('position_key')[x * 3:(x + 1) * 3])
    laws = BillsAndLaws.objects.all().order_by(F('assent_date').desc(nulls_last=True),
                                               F('stage_key').desc(nulls_last=True))[:6]
    passed_laws = (BillsAndLaws.objects.filter(stage_key__endswith='5') | BillsAndLaws.objects.filter(
        stage_key__endswith='6') | BillsAndLaws.objects.filter(stage_key__endswith='7')).count()
    awaiting_assent = (BillsAndLaws.objects.filter(stage_key__endswith='6') | BillsAndLaws.objects.filter(
        stage_key__endswith='5')).count()
    signed_laws = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
    signed_laws_percent = round((signed_laws / BillsAndLaws.objects.all().count()) * 100)
    passed_laws_percent = round((passed_laws / BillsAndLaws.objects.all().count()) * 100)
    print(passed_laws_percent)
    return render(request, 'home.html', {'members': members, 'login_status': login_status, 'laws': laws,
                                         'passed_laws_percent': passed_laws_percent,
                                         'signed_laws_percent': signed_laws_percent, 'signed_laws': signed_laws,
                                         'passed_laws': passed_laws, 'awaiting_assent': awaiting_assent})


def appstart(request):
    return render(request, 'index.html')


def portfolio(request, constituency):
    member = MemberInfo.objects.get(constituency=constituency)
    resume = MemberResume.objects.get(constituency=member.constituency)
    if member.othernames is None:
        member.othernames = ''
    return render(request, 'portfolio.html', {'member': member, 'resume': resume})


def member_area(request):
    if request.user.is_authenticated:
        user = request.user

        if user.username.startswith('hon.'):
            member = MemberInfo.objects.get(username=user.username)
            resume = MemberResume.objects.get(constituency=member.constituency)
            if member.othernames is None:
                member.othernames = ''
            return render(request, 'member_area.html', {'member': member, 'resume': resume})
        else:
            # messages.warning(request, "You don't have the required permissions for this page")
            return redirect('home')

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
    news = News.objects.all()
    return render(request, 'blog.html')


def news_detail(request):
    return render(request, 'blog-single.html')
