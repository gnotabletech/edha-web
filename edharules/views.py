from django.http import HttpResponse
from django.shortcuts import render
from .models import EDHARule


# Create your views here.
def index(request):
    rules = EDHARule.objects.all()
    sections = EDHARule.objects.all().values('rule_subsection_title', 'rule_section_num').distinct()
    section_list = []
    for section in sections:
        if section not in section_list:
            section_list.append(section)

    rules_count = EDHARule.objects.all().count()
    sections_count = EDHARule.objects.values('rule_subsection_num').distinct().count()
    subsections_count = EDHARule.objects.values('rule_section_num').distinct().count()
    return render(request, 'edharules/index.html',
                  {'rules': rules, 'sections': section_list, 'rules_count': rules_count,
                   'sections_count': sections_count, 'subsections_count': subsections_count})


def counter(request, value):
    rules = EDHARule.objects.get(pk=value)
    return render(request, 'edharules/rule-details.html', {'rules': rules})


def jumptosection(request, val):
    sections = EDHARule.objects.all().values('rule_subsection_title').distinct()
    section_list = []
    for section in sections:
        if section not in section_list:
            section_list.append(section)
    rules = EDHARule.objects.filter(rule_subsection_title=val)
    rules_count = EDHARule.objects.filter(rule_subsection_title=val).count()
    sections_count = EDHARule.objects.filter(rule_subsection_title=val).values(
        'rule_section_num').distinct().count()
    subsections_count = EDHARule.objects.filter(rule_subsection_title=val).values(
        'rule_subsection_num').distinct().count()
    return render(request, 'edharules/index.html',
                  {'rules': rules, 'sections': section_list, 'rules_count': rules_count,
                   'sections_count': sections_count, 'subsections_count': subsections_count})


def search(request):
    value = request.POST.get('info')
    print(value)
    rules = EDHARule.objects.filter(rule_details__icontains=value).order_by('rule_subsection_title')
    sections = EDHARule.objects.all().values('rule_subsection_title').distinct()
    section_list = []
    for section in sections:
        if section not in section_list:
            section_list.append(section)
    rules_count = EDHARule.objects.filter(rule_details__icontains=value).count()
    sections_count = EDHARule.objects.filter(rule_details__icontains=value).values(
        'rule_section_num').distinct().count()
    subsections_count = EDHARule.objects.filter(rule_details__icontains=value).values(
        'rule_subsection_num').distinct().count()
    return render(request, 'edharules/index.html',
                  {'rules': rules, 'sections': section_list, 'rules_count': rules_count,
                   'sections_count': sections_count, 'subsections_count': subsections_count})


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
