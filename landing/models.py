from django.db import models

# Create your models here.
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class StaffInfo(models.Model):
    ROLES = (('MP', 'MEMBER'),
             ('CH', 'CLERK OF THE HOUSE'),
             ('DCH', 'DEPUTY CLERK'),
             ('ES', 'SECRETARY TO THE COMMISSION'),
             ('HOD', 'HEAD OF DEPARTMENT'),
             ('STAFF', 'STAFF'),
             ('ADMIN', 'SYSTEM ADMIN'))
    DEPARTMENTS = (('ADMIN', 'ADMINISTRATION AND SUPPLIES'),
                   ('AUDIT', 'AUDIT'),
                   ('BUDGET', 'BUDGET'),
                   ('COMMISSION', 'COMMISSION'),
                   ('FINANCE', 'FINANCE AND ACCOUNTS'),
                   ('ICT', 'INFORMATION AND COMMUNICATION TECHNOLOGY'),
                   ('INFORMATION', 'INFORMATION'),
                   ('LEGAL', 'LEGAL SERVICES'),
                   ('LEGISLATIVE', 'LEGISLATIVE MATTERS'),
                   ('LIBRARY', 'LIBRARY AND ARCHIVES'),
                   ('MANPOWER', 'MANPOWER DEVELOPMENT AND TRAINING'),
                   ('CLERK', 'OFFICE OF THE CLERK'),
                   ('DEPUTY_SPK', 'OFFICE OF THE DEPUTY SPEAKER'),
                   ('SPK', 'OFFICE OF THE SPEAKER'),
                   ('PENSIONS', 'PENSIONS AND GRATUITY'),
                   ('PLANNING', 'PLANNING'),
                   ('PROTOCOL', 'PROTOCOL AND TRAVELS'),
                   ('PUB', 'PUBLICATIONS'),
                   ('RESEARCH', 'RESEARCH AND STATISTICS'),
                   ('WORKS', 'WORKS AND TECHNICAL SERVICES'))
    id = models.AutoField(db_column='ID', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=50)
    lastname = models.CharField(db_column='LastName', max_length=50)
    username = models.CharField(db_column='Username', unique=True, max_length=20)
    designation = models.CharField(db_column='Designation', max_length=50)
    role = models.CharField(db_column='Role', max_length=50, choices=ROLES, default='MP')
    department = models.CharField(db_column='Department', max_length=50, choices=DEPARTMENTS, default='ADMIN',
                                  blank=True, null=True)

    class Meta:
        db_table = 'StaffInfo'
        verbose_name_plural = "Staff Info"

    def save(self, *args, **kwargs):
        self.department = self.get_department_display()
        self.role = self.get_role_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lastname


class MemberInfo(models.Model):
    HIERARCHY = (('1', 'SPEAKER'),
                 ('2', 'DEPUTY SPEAKER'),
                 ('3', 'MAJORITY LEADER'),
                 ('4', 'CHIEF WHIP'),
                 ('5', 'MINORITY LEADER'),
                 ('6', 'DEPUTY LEADER'),
                 ('7', 'DEPUTY WHIP'),
                 ('8', 'MEMBER'))
    COMMITTEE = (('SP1', 'PUBLIC ACCOUNTS'),
                 ('SP2', 'RULES AND BUSINESS'),
                 ('SP3', 'SELECTION'),
                 ('SP4', 'TENDERS BOARD'),
                 ('SP5', 'HOUSE SERVICES'),
                 ('SP6', 'PUBLIC PETITIONS'),
                 ('ST1', 'APPROPRIATION AND PROJECT MONITORING'),
                 ('ST2', 'SECURITY'),
                 ('ST3', 'ETHICS AND PRIVILEGES'),
                 ('ST4', 'AGRICULTURE'),
                 ('ST5', 'INFORMATION, YOUTHS AND SPORTS'),
                 ('ST6', 'ARTS AND CULTURE'),
                 ('ST7', 'ENERGY AND WATER RESOURCES'),
                 ('ST8', 'OIL AND GAS'),
                 ('ST9', 'WOMEN AFFAIRS AND SOCIAL DEVELOPMENT'),
                 ('ST10', 'FINANCE AND ECONOMIC PLANNING'),
                 ('ST11', 'EDUCATION'),
                 ('ST12', 'WORKS AND PUBLIC UTILITIES'),
                 ('ST13', 'ENVIRONMENT AND TRANSPORT'),
                 ('ST14', 'JUDICIARY, HUMAN RIGHTS AND LEGAL MATTERS'),
                 ('ST15', 'COMMERCE AND INDUSTRY'),
                 ('ST16', 'LOCAL GOVERNMENTS AND CHIEFTAINCY AFFAIRS'),
                 ('ST17', 'LANDS AND SURVEY'),
                 ('ST18', 'HEALTH'))
    STATUS = (('1', 'INAUGURATED'),
              ('2', 'SWORN IN'),
              ('3', 'SERVING'),
              ('4', 'SUSPENDED'),
              ('5', 'IMPEACHED'),
              ('6', 'VACATED'),
              ('7', 'NULLIFIED'))
    LGA = (('1', 'AKOKO-EDO'),
           ('2', 'EGOR'),
           ('3', 'ESAN CENTRAL'),
           ('4', 'ESAN NORTH EAST'),
           ('5', 'ESAN SOUTH EAST'),
           ('6', 'ESAN WEST'),
           ('7', 'ETSAKO CENTRAL'),
           ('8', 'ETSAKO EAST'),
           ('9', 'ETSAKO WEST'),
           ('10', 'IGUEBEN'),
           ('11', 'IKPOBA-OKHA'),
           ('12', 'OREDO'),
           ('13', 'ORHIONMWON'),
           ('14', 'OVIA NORTH EAST'),
           ('15', 'OVIA SOUTH WEST'),
           ('16', 'OWAN EAST'),
           ('17', 'OWAN WEST'),
           ('18', 'UHUNMWODE'))
    CONSTITUENCIES = (('1', 'AKOKO-EDO I'),
                      ('2', 'AKOKO-EDO II'),
                      ('3', 'EGOR'),
                      ('4', 'ESAN CENTRAL'),
                      ('5', 'ESAN NORTH EAST I'),
                      ('6', 'ESAN NORTH EAST II'),
                      ('7', 'ESAN SOUTH EAST'),
                      ('8', 'ESAN WEST'),
                      ('9', 'ETSAKO CENTRAL'),
                      ('10', 'ETSAKO EAST'),
                      ('11', 'ETSAKO WEST I'),
                      ('12', 'ETSAKO WEST II'),
                      ('13', 'IGUEBEN'),
                      ('14', 'IKPOBA-OKHA'),
                      ('15', 'OREDO EAST'),
                      ('16', 'OREDO WEST'),
                      ('17', 'ORHIONMWON I'),
                      ('18', 'ORHIONMWON II'),
                      ('19', 'OVIA NORTH EAST I'),
                      ('20', 'OVIA NORTH EAST II'),
                      ('21', 'OVIA SOUTH WEST'),
                      ('22', 'OWAN EAST'),
                      ('23', 'OWAN WEST'),
                      ('24', 'UHUNMWODE'))
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=20)
    position = models.CharField(max_length=15, choices=HIERARCHY, default='8')
    position_key = models.IntegerField(choices=HIERARCHY, default='8')
    qualifications = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50, choices=CONSTITUENCIES, default='1')
    lga = models.CharField(max_length=50, choices=LGA, default='1')
    date_of_birth = models.DateField()
    age = models.IntegerField()
    profile_description = models.CharField(max_length=50)
    tenure = models.CharField(max_length=50)
    party = models.CharField(max_length=50)
    tenure_start = models.DateField(default=timezone.now)
    email = models.EmailField()
    projects = models.TextField(max_length=150)
    status = models.CharField(max_length=11, choices=STATUS, default='1')
    committee = models.CharField(max_length=50, choices=COMMITTEE, default='SP1', blank=True, null=True)
    committee_key = models.CharField(max_length=4, choices=COMMITTEE, default='SP1', blank=True, null=True)
    twitter_account = models.CharField(max_length=50)
    facebook_account = models.CharField(max_length=50)
    instagram_account = models.CharField(max_length=50)
    linkedin_account = models.CharField(max_length=50)
    phone = PhoneNumberField(null=True, blank=True)

    class Meta:
        db_table = 'MemberInfo'
        verbose_name_plural = "Member Info"

    def save(self, *args, **kwargs):
        self.committee = self.get_committee_display()
        self.position = self.get_position_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lastname
