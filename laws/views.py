import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from edharulesandbiz.settings import BASE_DIR
from .models import BillsAndLaws, AdminInfo


# Create your views here.
def laws_repo(request):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.all().order_by('assent_date')
        laws_count = BillsAndLaws.objects.all().count()
        assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
        pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
        awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
        return render(request, 'laws/index.html',
                      {'user': user, 'laws': laws, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count})
    else:
        return redirect('login')


def getlaw(request):
    if request.method == 'POST':
        request.session['searchstring'] = request.POST.get('inputTitle')

    if request.user.is_authenticated:
        request.session.get('searchstring')
        user = request.user
        laws = BillsAndLaws.objects.filter(title__icontains=request.session.get('searchstring')).order_by('assent_date')
        laws_count = BillsAndLaws.objects.all().count()
        assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
        pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
        awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
        return render(request, 'laws/index.html',
                      {'laws': laws, 'user': user, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count})
    else:
        return redirect('login_user_quicksearch')

