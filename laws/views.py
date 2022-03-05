import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from edharulesandbiz.settings import BASE_DIR
from .models import BillsAndLaws, AdminInfo


# Create your views here.
def laws_repo(request):
    user = AdminInfo.objects.all().get(username='notaigbe')
    laws = BillsAndLaws.objects.all().order_by('assent_date')
    laws_count = BillsAndLaws.objects.all().count()
    assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
    pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
    awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
    return render(request, 'laws/index.html',
                  {'user': user, 'laws': laws, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                   'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count})


def getlaw(request):
    value = request.POST.get('inputTitle')
    user = AdminInfo.objects.get(username='notaigbe')
    laws = BillsAndLaws.objects.filter(title__icontains=value).order_by('assent_date')
    laws_count = BillsAndLaws.objects.all().count()
    assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
    pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
    awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
    return render(request, 'laws/index.html',
                  {'laws': laws, 'user': user, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                   'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'laws/signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'laws/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, 'index.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})
