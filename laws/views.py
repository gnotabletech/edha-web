import math
import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import F, Q
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from edharulesandbiz.settings import BASE_DIR
from .models import BillsAndLaws, AdminInfo


# Create your views here.
def laws_repo(request):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.all().order_by(F('assent_date').desc(nulls_last=True),
                                                   F('stage_key').desc(nulls_last=True))[:10]
        laws_count = BillsAndLaws.objects.all().count()
        pages = BillsAndLaws.objects.all()[:laws_count:10]
        assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
        pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
        awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()

        return render(request, 'laws/index.html',
                      {'user': user, 'laws': laws, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count,
                       'pages': pages})
    else:
        return redirect('login')


def laws_repo_more(request, last_record):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.all().order_by(F('assent_date').desc(nulls_last=True))[
               int(last_record):int(last_record) + 10]
        laws_count = BillsAndLaws.objects.all().count()
        pages = BillsAndLaws.objects.all()[:laws_count:10]
        assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
        pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
        awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
        return render(request, 'laws/index.html',
                      {'user': user, 'laws': laws, 'laws_count': laws_count,
                       'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count,
                       'pages': pages})
    else:
        return redirect('login')


def getlaw(request):
    if request.method == 'POST':
        request.session['searchstring'] = request.POST.get('inputTitle')

    if request.user.is_authenticated:
        request.session.get('searchstring')
        user = request.user
        laws = BillsAndLaws.objects.filter(title__icontains=request.session.get('searchstring')).order_by(
            F('assent_date').desc(nulls_last=True)) | BillsAndLaws.objects.filter(
            short_title__icontains=request.session.get('searchstring')).order_by(F('assent_date').desc(nulls_last=True))
        laws_count = BillsAndLaws.objects.all().count()
        assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
        pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
        awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
        return render(request, 'laws/index.html',
                      {'laws': laws, 'user': user, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count})
    else:
        return redirect('login_user_quicksearch')


def print_law(request):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.all().order_by(F('assent_date').desc(nulls_last=True),
                                                   F('stage_key').desc(nulls_last=True))
        law_count = []
        assented_laws_count = []
        pending_laws_count = []
        chart_label = []
        base_year = 1991
        assemblies = math.ceil((timezone.now().year - base_year) / 4)
        print(assemblies)
        for assembly in range(assemblies):
            assembly_start = base_year + (4 * assembly)
            assembly_end = assembly_start + 4
            print(f'{assembly_start} to {assembly_end}')

            law_count.append(BillsAndLaws.objects.filter(Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).count())
            pending_laws_count.append(BillsAndLaws.objects.filter(Q(publication__year__gte=assembly_start,
                                                                    publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).exclude(
                stage='ASSENTED TO').count())
            assented_laws_count.append(BillsAndLaws.objects.filter(Q(assent_date__year__gte=assembly_start,
                                                                     assent_date__year__lte=assembly_end) | Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end)).filter(
                stage='ASSENTED TO').count())
            chart_label.append(assembly + 1)
            print(assented_laws_count)
        print(chart_label)
        return render(request, 'laws/list.html',
                      {'user': user, 'laws': laws, 'law_count': law_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'chart_label': chart_label})
    else:
        return redirect('login')


def print_law_report(request):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.all().order_by(F('assent_date').desc(nulls_last=True),
                                                   F('stage_key').desc(nulls_last=True))
        law_count = []
        assented_laws_count = []
        pending_laws_count = []
        chart_label = []
        base_year = 1991
        assemblies = math.ceil((timezone.now().year - base_year) / 4)
        print(assemblies)
        for assembly in range(assemblies):
            assembly_start = base_year + (4 * assembly)
            assembly_end = assembly_start + 4
            print(f'{assembly_start} to {assembly_end}')

            law_count.append(BillsAndLaws.objects.filter(Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).count())
            pending_laws_count.append(BillsAndLaws.objects.filter(Q(publication__year__gte=assembly_start,
                                                                    publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).exclude(
                stage='ASSENTED TO').count())
            assented_laws_count.append(BillsAndLaws.objects.filter(Q(assent_date__year__gte=assembly_start,
                                                                     assent_date__year__lte=assembly_end) | Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end)).filter(
                stage='ASSENTED TO').count())
            chart_label.append(assembly + 1)
        title = "DETAILED REPORT OF BILLS AND LAWS"
        return render(request, 'laws/bills_report.html',
                      {'user': user, 'laws': laws, 'law_count': law_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'title': title, 'chart_label': chart_label})
    else:
        return redirect('login')


def print_pending_bills(request):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.exclude(stage="ASSENTED TO").order_by(F('publication').desc(nulls_last=True),
                                                                          F('stage_key').desc(nulls_last=True))
        law_count = []
        assented_laws_count = []
        pending_laws_count = []
        chart_label = []
        base_year = 1991
        assemblies = math.ceil((timezone.now().year - base_year) / 4)
        print(assemblies)
        for assembly in range(assemblies):
            assembly_start = base_year + (4 * assembly)
            assembly_end = assembly_start + 4
            print(f'{assembly_start} to {assembly_end}')

            law_count.append(BillsAndLaws.objects.filter(Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).count())
            pending_laws_count.append(BillsAndLaws.objects.filter(Q(publication__year__gte=assembly_start,
                                                                    publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).exclude(
                stage='ASSENTED TO').count())
            assented_laws_count.append(BillsAndLaws.objects.filter(Q(assent_date__year__gte=assembly_start,
                                                                     assent_date__year__lte=assembly_end) | Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end)).filter(
                stage='ASSENTED TO').count())
            chart_label.append(assembly + 1)

        title = "DETAILED REPORT OF PENDING BILLS"
        return render(request, 'laws/bills_report.html',
                      {'user': user, 'laws': laws, 'law_count': law_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'title': title, 'chart_label': chart_label})
    else:
        return redirect('login')


def print_assented_laws(request):
    if request.user.is_authenticated:
        user = request.user
        laws = BillsAndLaws.objects.filter(stage="ASSENTED TO").order_by(F('assent_date').desc(nulls_last=True),
                                                                         F('stage_key').desc(nulls_last=True))
        law_count = []
        assented_laws_count = []
        pending_laws_count = []
        chart_label = []
        base_year = 1991
        assemblies = math.ceil((timezone.now().year - base_year) / 4)
        print(assemblies)
        for assembly in range(assemblies):
            assembly_start = base_year + (4 * assembly)
            assembly_end = assembly_start + 4
            print(f'{assembly_start} to {assembly_end}')

            law_count.append(BillsAndLaws.objects.filter(Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).count())
            pending_laws_count.append(BillsAndLaws.objects.filter(Q(publication__year__gte=assembly_start,
                                                                    publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end) | Q(assent_date__year__gte=assembly_start,
                                                           assent_date__year__lte=assembly_end)).exclude(
                stage='ASSENTED TO').count())
            assented_laws_count.append(BillsAndLaws.objects.filter(Q(assent_date__year__gte=assembly_start,
                                                                     assent_date__year__lte=assembly_end) | Q(
                publication__year__gte=assembly_start,
                publication__year__lte=assembly_end) | Q(
                third_reading__year__gte=assembly_start,
                third_reading__year__lte=assembly_end)).filter(
                stage='ASSENTED TO').count())
            chart_label.append(assembly + 1)
        print(chart_label)
        title = "DETAILED REPORT OF ASSENTED LAWS"
        return render(request, 'laws/bills_report.html',
                      {'user': user, 'laws': laws, 'law_count': law_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'chart_label': chart_label, 'title': title})
    else:
        return redirect('login')


def get_law_by_assembly(request):
    if request.user.is_authenticated:
        user = request.user
        laws = []
        law_count = []
        assented_laws_count = []
        pending_laws_count = []
        chart_label = []
        base_year = 1991
        assemblies = math.ceil((timezone.now().year - base_year) / 4)
        print(assemblies)
        for assembly in range(assemblies):
            assembly_start = base_year + (4 * assembly)
            assembly_end = assembly_start + 4
            print(f'{assembly_start} to {assembly_end}')
            laws = BillsAndLaws.objects.filter(assent_date__year__gte=assembly_start,
                                               assent_date__year__lte=assembly_end).order_by(
                F('assent_date').desc(nulls_last=True),
                F('stage_key').desc(nulls_last=True))

            law_count.append(BillsAndLaws.objects.filter(assent_date__year__gte=assembly_start,
                                                         assent_date__year__lte=assembly_end).count())
            pending_laws_count.append(BillsAndLaws.objects.filter(assent_date__year__gte=assembly_start,
                                                                  assent_date__year__lte=assembly_end).exclude(
                stage='ASSENTED TO').count())
            assented_laws_count.append(BillsAndLaws.objects.filter(assent_date__year__gte=assembly_start,
                                                                   assent_date__year__lte=assembly_end).filter(
                stage='ASSENTED TO').count())
            chart_label.append(assembly + 1)
        return render(request, 'laws/list.html',
                      {'user': user, 'assented_laws': laws, 'law_count': law_count,
                       'pending_laws_count': pending_laws_count, 'assented_laws_count': assented_laws_count,
                       'chart_label': chart_label})
    else:
        return redirect('login')
