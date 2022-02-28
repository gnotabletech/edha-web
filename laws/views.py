import os

from django.http import FileResponse
from django.shortcuts import render

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
    return render(request, 'laws/userHome.html',
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
    return render(request, 'laws/userHome.html',
                  {'laws': laws, 'user': user, 'laws_count': laws_count, 'assented_laws_count': assented_laws_count,
                   'pending_laws_count': pending_laws_count, 'awaiting_assent_count': awaiting_assent_count})


def display_law(request, value):
    filepath = os.path.join('static', 'assets/laws/' + value.strip() + '.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
