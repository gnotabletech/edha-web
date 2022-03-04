# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone

from edharulesandbiz import settings


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class BillsAndLaws(models.Model):
    STAGES = (('STAGE1', 'PUBLICATION'),
              ('STAGE2', 'FIRST READING'),
              ('STAGE3', 'SECOND READING'),
              ('STAGE4', 'COMMITTEE STAGE'),
              ('STAGE5', 'THIRD READING'),
              ('STAGE6', 'AWAITING ASSENT'),
              ('STAGE7', 'ASSENTED TO'),
              ('STAGE8', 'ASSENT DENIED'))
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE', unique=True, max_length=500)  # Field name made lowercase.
    assent_date = models.DateField(db_column='ASSENT_DATE', blank=True, null=True)  # Field name made lowercase.
    stage = models.CharField(db_column='STAGE', max_length=20, choices=STAGES,
                             default='STAGE1')  # Field name made lowercase.
    sponsor = models.CharField(db_column='SPONSOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_reading = models.DateField(db_column='FIRST_READING', blank=True, null=True)  # Field name made lowercase.
    second_reading = models.DateField(db_column='SECOND_READING', blank=True, null=True)  # Field name made lowercase.
    committee_date = models.DateField(db_column='COMMITTEE_DATE', blank=True, null=True)  # Field name made lowercase.
    referred_committee = models.CharField(db_column='REFERRED_COMMITTEE', max_length=100, blank=True,
                                          null=True)  # Field name made lowercase.
    third_reading = models.DateField(db_column='THIRD_READING', blank=True, null=True)  # Field name made lowercase.
    publication = models.DateField(db_column='PUBLICATION', blank=True, null=True)  # Field name made lowercase.
    short_title = models.TextField(db_column='SHORT_TITLE', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    document = models.FileField(upload_to='files', default=timezone.now, storage=OverwriteStorage)

    class Meta:
        # managed = False
        db_table = 'Bills_and_Laws'

    def save(self, *args, **kwargs):
        self.document = f'{self.short_title}.pdf'.replace('/', '_').replace(') (', '_').replace(') ', '_').replace(' (', '_').replace(
            ', ', '_').replace(' ', '_')
        self.stage = self.stage.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class AdminInfo(models.Model):
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
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=20)  # Field name made lowercase.
    pword = models.CharField(db_column='Pword', max_length=20)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=50)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50, choices=ROLES, default='MP')  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, choices=DEPARTMENTS, default='ADMIN',
                                  blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AdminInfo'

    def save(self, *args, **kwargs):
        self.department = self.department.name
        self.role = self.role.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lastname
