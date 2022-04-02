from django.db.models import F
from django.shortcuts import render, redirect


from .models import BillsAndLaws


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
        laws = BillsAndLaws.objects.filter(title__contains=request.session.get('searchstring')).order_by(
            F('assent_date').desc(nulls_last=True), F('stage_key').desc(nulls_last=True)) | BillsAndLaws.objects.filter(
            short_title__contains=request.session.get('searchstring')).order_by(F('assent_date').desc(nulls_last=True),
                                                                                F('stage_key').desc(nulls_last=True))
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
        laws_count = BillsAndLaws.objects.all().count()
        pages = BillsAndLaws.objects.all()[:laws_count:10]
        assented_laws_count = BillsAndLaws.objects.filter(stage='ASSENTED TO').count()
        pending_laws_count = BillsAndLaws.objects.exclude(stage='ASSENTED TO').count()
        awaiting_assent_count = BillsAndLaws.objects.filter(stage='AWAITING ASSENT').count()
        return render(request, 'laws/list.html',
                      {'user': user, 'laws': laws, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                       'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count,
                       'pages': pages})
    else:
        return redirect('login')


