from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from laws.models import OverwriteStorage


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
    # firstname = models.CharField(db_column='FirstName', max_length=50)
    # lastname = models.CharField(db_column='LastName', max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return self.username


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
              ('7', 'NULLIFIED'),
              ('8', 'PENDING'))
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
    TENURE = (('1st', 'FIRST'),
              ('2nd', 'SECOND'),
              ('3rd', 'THIRD'),
              ('4th', 'FOURTH'))
    PARTY = (('PDP', 'PEOPLES DEMOCRATIC PARTY'),
             ('APC', 'ALL PROGRESSIVES CONGRESS'),
             ('APGA', 'ALL PROGRESSIVES GRAND ALLIANCE'),
             ('YPP', 'YOUNG PROGRESSIVES PARTY'),
             ('ADC', 'AFRICAN DEMOCRATIC CONGRESS'),
             ('PRP', 'PEOPLES REDEMPTION PARTY'),
             ('ZLP', 'ZENITH LABOUR PARTY'),
             ('ADP', 'ACTION DEMOCRATIC PARTY'),
             ('NNPP', 'NEW NIGERIA PEOPLES PARTY'),
             ('A', 'ACCORD PARTY'),
             ('AA', 'ACTION ALLIANCE'),
             ('AAC', 'AFRICAN ACTION CONGRESS'),
             ('APP', 'ALLIED PEOPLES PARTY'),
             ('BP', 'BOOT PARTY'),
             ('LP', 'LABOUR PARTY'),
             ('NRM', 'NATIONAL RESCUE MOVEMENT'),
             ('SDP', 'SOCIAL DEMOCRATIC PARTY'))
    # id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    othernames = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(unique=True, max_length=25)
    position = models.CharField(max_length=15, choices=HIERARCHY, default='8')
    position_key = models.CharField(max_length=1, choices=HIERARCHY, default='8')
    qualifications = models.CharField(max_length=50, blank=True, null=True)
    constituency = models.CharField(primary_key=True, max_length=50, unique=True, default='1')
    lga = models.CharField(max_length=50, choices=LGA, default='1', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    profile_description = models.CharField(max_length=50, blank=True, null=True)
    tenure = models.CharField(max_length=3, choices=TENURE, blank=True, null=True)
    party = models.CharField(max_length=150, choices=PARTY, blank=True, null=True)
    party_key = models.CharField(max_length=4, choices=PARTY, blank=True, null=True)
    tenure_start = models.DateField(default=timezone.now)
    email = models.EmailField(blank=True, null=True)
    projects = models.TextField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=11, choices=STATUS, default='1')
    committee = models.CharField(max_length=50, choices=COMMITTEE, default='SP1', blank=True, null=True)
    committee_key = models.CharField(max_length=4, choices=COMMITTEE, default='SP1', blank=True, null=True)
    twitter_account = models.CharField(max_length=50, blank=True, null=True)
    facebook_account = models.CharField(max_length=50, blank=True, null=True)
    instagram_account = models.CharField(max_length=50, blank=True, null=True)
    linkedin_account = models.CharField(max_length=50, blank=True, null=True)
    phone = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    cover_image = models.ImageField(upload_to='profile/', blank=True)
    public_image = models.ImageField(upload_to='profile/', blank=True)

    class Meta:
        db_table = 'MemberInfo'
        verbose_name_plural = "Members Info"

    def save(self, *args, **kwargs):
        self.committee = self.get_committee_display()
        self.position = self.get_position_display()
        self.party = self.get_party_display()
        self.public_image = f'media/profile/{self.constituency}_public.jpg'.replace(' ', '_').lower()
        self.profile_image = f'media/profile/{self.constituency}_profile.jpg'.replace(' ', '_').lower()
        self.cover_image = f'media/profile/{self.constituency}_cover.jpg'.replace(' ', '_').lower()
        # self.constituency = self.get_constituency_display()
        # self.username = self.username.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.constituency


class Resume(models.Model):
    DEGREE = (('FSLC', 'FIRST SCHOOL LEAVING CERTIFICATE'),
              ('SSCE', 'SENIOR SCHOOL CERTIFICATE'),
              ('OND', 'ORDINARY NATIONAL DIPLOMA'),
              ('HND', 'HIGHER NATIONAL DIPLOMA'),
              ('B.SC', 'BACHELOR OF SCIENCE'),
              ('BPA', 'BACHELORS IN PUBLIC ADMINISTRATION'),
              ('BA', 'BACHELOR OF ARTS'),
              ('MBA', 'MASTER OF BUSINESS ADMINISTRATION'),
              ('MPA', 'MASTERS IN PUBLIC ADMINISTRATION'),
              ('B.Ed', 'BACHELOR OF EDUCATION'),
              ('M.Ed', 'MASTER OF EDUCATION'),
              ('B.Eng', 'BACHELOR OF ENGINEERING'),
              ('M.Eng', 'MASTER OF ENGINEERING'),
              ('LL.B', 'BACHELOR OF LAWS'),
              ('LL.M', 'MASTER OF LAWS'),
              ('PGD', 'POSTGRADUATE DIPLOMA'),
              ('B.Tech', 'BACHELOR OF TECHNOLOGY'),
              ('M.Tech', 'MASTER OF TECHNOLOGY'),
              ('B.Pharm', 'BACHELOR OF PHARMACY'),
              ('M.Pharm', 'MASTER OF PHARMACY'),
              ('P.hD', 'DOCTOR OF PHILOSOPHY'),)

    id = models.AutoField(primary_key=True)
    # firstname = models.CharField(max_length=50, blank=True, null=True)
    # lastname = models.CharField(max_length=50, blank=True, null=True)
    # othernames = models.CharField(max_length=50, blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_1 = models.CharField(max_length=50, choices=DEGREE, default='SSCE')
    course_1 = models.CharField(max_length=50, blank=True)
    institution_1 = models.CharField(max_length=100, blank=True)
    degree_1_key = models.CharField(max_length=7, choices=DEGREE, default='SSCE')
    degree_1_date = models.DateField(blank=True, null=True)
    degree_2 = models.CharField(max_length=50, choices=DEGREE, default='SSCE')
    course_2 = models.CharField(max_length=50, blank=True)
    institution_2 = models.CharField(max_length=100, blank=True)
    degree_2_key = models.CharField(max_length=7, choices=DEGREE, default='SSCE')
    degree_2_date = models.DateField(blank=True, null=True)
    degree_3 = models.CharField(max_length=50, choices=DEGREE, default='SSCE')
    course_3 = models.CharField(max_length=50, blank=True)
    institution_3 = models.CharField(max_length=100, blank=True)
    degree_3_key = models.CharField(max_length=7, choices=DEGREE, default='SSCE')
    degree_3_date = models.DateField(blank=True, null=True)
    experience_1 = models.CharField(max_length=50, blank=True, null=True)
    experience_1_office = models.CharField(max_length=50, blank=True, null=True)
    experience_1_duty = models.TextField()
    experience_1_date = models.DateField(blank=True, null=True)
    experience_2 = models.CharField(max_length=50, blank=True, null=True)
    experience_2_office = models.CharField(max_length=50, blank=True, null=True)
    experience_2_duty = models.TextField()
    experience_2_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Resume'
        verbose_name_plural = "Resumes"

    def save(self, *args, **kwargs):
        self.degree_1 = self.get_degree_1_display()
        self.degree_2 = self.get_degree_2_display()
        self.degree_3 = self.get_degree_3_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class MemberResume(models.Model):
    DEGREE = (('FSLC', 'FIRST SCHOOL LEAVING CERTIFICATE'),
              ('SSCE', 'SENIOR SCHOOL CERTIFICATE'),
              ('OND', 'ORDINARY NATIONAL DIPLOMA'),
              ('HND', 'HIGHER NATIONAL DIPLOMA'),
              ('B.SC', 'BACHELOR OF SCIENCE'),
              ('BPA', 'BACHELORS IN PUBLIC ADMINISTRATION'),
              ('BA', 'BACHELOR OF ARTS'),
              ('MBA', 'MASTER OF BUSINESS ADMINISTRATION'),
              ('MPA', 'MASTERS IN PUBLIC ADMINISTRATION'),
              ('B.Ed', 'BACHELOR OF EDUCATION'),
              ('M.Ed', 'MASTER OF EDUCATION'),
              ('B.Eng', 'BACHELOR OF ENGINEERING'),
              ('M.Eng', 'MASTER OF ENGINEERING'),
              ('LL.B', 'BACHELOR OF LAWS'),
              ('LL.M', 'MASTER OF LAWS'),
              ('PGD', 'POSTGRADUATE DIPLOMA'),
              ('B.Tech', 'BACHELOR OF TECHNOLOGY'),
              ('M.Tech', 'MASTER OF TECHNOLOGY'),
              ('B.Pharm', 'BACHELOR OF PHARMACY'),
              ('M.Pharm', 'MASTER OF PHARMACY'),
              ('P.hD', 'DOCTOR OF PHILOSOPHY'),)

    id = models.AutoField(primary_key=True)
    # firstname = models.CharField(max_length=50, blank=True, null=True)
    # lastname = models.CharField(max_length=50, blank=True, null=True)
    # othernames = models.CharField(max_length=50, blank=True, null=True)
    constituency = models.OneToOneField(MemberInfo, on_delete=models.CASCADE, unique=True, default='1')
    degree_1 = models.CharField(max_length=50, choices=DEGREE, default='SSCE', blank=True, null=True)
    course_1 = models.CharField(max_length=50, blank=True, null=True)
    institution_1 = models.CharField(max_length=100, blank=True, null=True)
    degree_1_key = models.CharField(max_length=7, choices=DEGREE, default='SSCE', blank=True, null=True)
    degree_1_date = models.DateField(blank=True, null=True)
    degree_2 = models.CharField(max_length=50, choices=DEGREE, default='SSCE', blank=True, null=True)
    course_2 = models.CharField(max_length=50, blank=True, null=True)
    institution_2 = models.CharField(max_length=100, blank=True, null=True)
    degree_2_key = models.CharField(max_length=7, choices=DEGREE, default='SSCE', blank=True, null=True)
    degree_2_date = models.DateField(blank=True, null=True)
    degree_3 = models.CharField(max_length=50, choices=DEGREE, default='SSCE', blank=True, null=True)
    course_3 = models.CharField(max_length=50, blank=True, null=True)
    institution_3 = models.CharField(max_length=100, blank=True, null=True)
    degree_3_key = models.CharField(max_length=7, choices=DEGREE, default='SSCE', blank=True, null=True)
    degree_3_date = models.DateField(blank=True, null=True)
    experience_1 = models.CharField(max_length=50, blank=True, null=True)
    experience_1_office = models.CharField(max_length=50, blank=True, null=True)
    experience_1_duty = models.TextField(blank=True, null=True)
    experience_1_date = models.DateField(blank=True, null=True)
    experience_2 = models.CharField(max_length=50, blank=True, null=True)
    experience_2_office = models.CharField(max_length=50, blank=True, null=True)
    experience_2_duty = models.TextField(blank=True, null=True)
    experience_2_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'MemberResume'
        verbose_name_plural = "Members Resumes"

    def save(self, *args, **kwargs):
        self.degree_1 = self.get_degree_1_display()
        self.degree_2 = self.get_degree_2_display()
        self.degree_3 = self.get_degree_3_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class News(models.Model):
    id = models.AutoField(primary_key=True)
    # firstname = models.CharField(max_length=50, blank=True, null=True)
    # lastname = models.CharField(max_length=50, blank=True, null=True)
    # othernames = models.CharField(max_length=50, blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    news_date = models.DateField(blank=True, null=True)
    news_title = models.CharField(max_length=50, blank=True, null=True)
    news_details = models.TextField(blank=True, null=True)
    desc_photo = models.CharField(max_length=50, default='1', blank=True, null=True)

    class Meta:
        db_table = 'News'
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        self.desc_photo = f'{self.news_title}_{self.news_date}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.news_title


class Resources(models.Model):
    id = models.AutoField(primary_key=True)
    vp_date = models.DateField(blank=True, null=True)
    vp_file = models.FileField(upload_to='files', default=timezone.now, storage=OverwriteStorage)
    official_report_date = models.DateField(blank=True, null=True)
    official_report_file = models.FileField(upload_to='files', default=timezone.now, storage=OverwriteStorage)
    order_paper_date = models.DateField(blank=True, null=True)
    order_paper_file = models.FileField(upload_to='files', default=timezone.now, storage=OverwriteStorage)

    class Meta:
        db_table = 'Resources'
        verbose_name_plural = "Resources"

    def save(self, *args, **kwargs):
        self.vp_file = f'{self.vp_date}.pdf'
        self.official_report_file = f'{self.official_report_date}.pdf'
        self.order_paper_file = f'{self.order_paper_date}.pdf'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_paper_date
