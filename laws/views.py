import os

from django.http import FileResponse
from django.shortcuts import render

from edharulesandbiz.settings import BASE_DIR
from .models import BillsAndLaws, AdminInfo


# Create your views here.
def laws_repo(request):
    user = AdminInfo.objects.all().get(username='notaigbe')
    laws = BillsAndLaws.objects.all().order_by('assent_date')
    return render(request, 'laws/userHome.html', {'user': user, 'laws': laws})


def getlaw(request):
    value = request.POST.get('inputTitle')
    user = AdminInfo.objects.get(username='notaigbe')
    laws = BillsAndLaws.objects.filter(short_title__icontains=value).order_by('assent_date')
    return render(request, 'laws/userHome.html', {'laws': laws, 'user': user})


def display_law(request, value):
    if value != '':
        filepath = os.path.join('static', 'assets/laws/' + value.strip() + '.pdf')
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
