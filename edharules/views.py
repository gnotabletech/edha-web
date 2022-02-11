from django.http import HttpResponse
from django.shortcuts import render
from .models import EDHARules


# Create your views here.
def index(request):
    rules = EDHARules.objects.all()
    sections = EDHARules.objects.all().values('rule_subsection_title').distinct()
    rules_count = EDHARules.objects.all().count()
    sections_count = EDHARules.objects.values('rule_section_title').distinct().count()
    subsections_count = EDHARules.objects.values('rule_subsection_title').distinct().count()
    return render(request, 'index.html', {'rules': rules, 'sections': sections, 'rules_count': rules_count,
                                          'sections_count': sections_count, 'subsections_count': subsections_count})


def counter(request, value):
    rules = EDHARules.objects.get(pk=value)
    return render(request, 'rule-details.html', {'rules': rules})


def jumptosection(request, val):
    sections = EDHARules.objects.all().values('rule_subsection_title').distinct()
    rules = EDHARules.objects.filter(rule_subsection_title=val)
    rules_count = EDHARules.objects.filter(rule_subsection_title=val).count()
    sections_count = EDHARules.objects.filter(rule_subsection_title=val).values(
        'rule_section_title').distinct().count()
    subsections_count = EDHARules.objects.filter(rule_subsection_title=val).values(
        'rule_subsection_title').distinct().count()
    return render(request, 'index.html', {'rules': rules, 'sections': sections, 'rules_count': rules_count,
                                          'sections_count': sections_count, 'subsections_count': subsections_count})


def search(request):
    value = request.POST.get('info')
    rules = EDHARules.objects.filter(rule_details__icontains=value)
    sections = EDHARules.objects.all().values('rule_subsection_title').distinct()
    rules_count = EDHARules.objects.filter(rule_details__icontains=value).count()
    sections_count = EDHARules.objects.filter(rule_details__icontains=value).values(
        'rule_section_title').distinct().count()
    subsections_count = EDHARules.objects.filter(rule_details__icontains=value).values(
        'rule_subsection_title').distinct().count()
    return render(request, 'index.html', {'rules': rules, 'sections': sections, 'rules_count': rules_count,
                                          'sections_count': sections_count, 'subsections_count': subsections_count})
