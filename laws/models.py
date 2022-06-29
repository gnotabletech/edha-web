# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import os
import subprocess

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request
from django.utils import timezone
from wand.image import Image
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
              ('STAGE9', 'PUBLIC HEARING'),
              ('STAGE5', 'THIRD READING'),
              ('STAGE6', 'AWAITING ASSENT'),
              ('STAGE7', 'ASSENTED TO'),
              ('STAGE8', 'ASSENT DENIED'))
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='title', unique=True, max_length=500)  # Field name made lowercase.
    assent_date = models.DateField(db_column='assent_date', blank=True, null=True)  # Field name made lowercase.
    stage = models.CharField(db_column='stage', max_length=20, choices=STAGES,
                             default='STAGE1')  # Field name made lowercase.
    stage_key = models.CharField(max_length=6, choices=STAGES, default='STAGE1')  # Field name made lowercase.
    sponsor = models.CharField(db_column='sponsor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_reading = models.DateField(db_column='first_reading', blank=True, null=True)  # Field name made lowercase.
    second_reading = models.DateField(db_column='second_reading', blank=True, null=True)  # Field name made lowercase.
    committee_date = models.DateField(db_column='committee_date', blank=True, null=True)  # Field name made lowercase.
    referred_committee = models.CharField(db_column='referred_committee', max_length=100, blank=True,
                                          null=True)  # Field name made lowercase.
    third_reading = models.DateField(db_column='third_reading', blank=True, null=True)  # Field name made lowercase.
    publication = models.DateField(db_column='publication', blank=True, null=True)  # Field name made lowercase.
    short_title = models.TextField(db_column='short_title', blank=True,
                                   null=True)  # Field name made lowercase.
    document = models.FileField(upload_to='media', default='unavailable.pdf')
    document_thumbnail = models.ImageField(upload_to='media/thumbnails', blank=True,
                                           null=True, default='unavailable.jpg')

    class Meta:
        # managed = False
        db_table = 'bills_and_laws'
        verbose_name_plural = "Bills and Laws"

    def save(self, *args, **kwargs):
        # self.document = f'{self.short_title}.pdf'.replace('/', '_').replace(') (', '_').replace(') ', '_').replace(' (',
        #                                                                                                           '_').replace(
        #    ', ', '_').replace(' ', '_').replace(')', '_').replace('(', '_')
        #thumbnail = Image(filename=request.FILES)
        #document_thumbnail_converted = thumbnail.convert('jpg')
        #self.document_thumbnail.save(f'media/thumbnail/{str(request.FILES)}'.replace('.pdf','.jpg'), document_thumbnail_converted[0])
        self.stage = self.get_stage_key_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_save, sender=BillsAndLaws)
def update_thumbnail(sender, instance, **kwargs):
#    """This post save function creates a thumbnail for the commentary PDF"""
    temp = BillsAndLaws.objects.get(pk=instance.pk)
    thumbnail = Image(temp.document)
    thumbnail_converted = thumbnail.convert('jpg')
    print(thumbnail_converted)
    print(thumbnail_converted[0])
    print(thumbnail_converted.sequence[0])
    #temp.update(document_thumbnail= thumbnail[0])
#    pdf = request.FILES
#    document_thumbnail = Image(filename=request.FILES)
#    document_thumbnail_converted = document_thumbnail.convert('jpg')
    # document_thumbnail_converted[0].save(filename=f'{instance.document}'.replace('.pdf', '.jpg').replace('media/','media/thumbnails'))
    # for img in document_thumbnail_converted.sequence:
    #    page = document_thumbnail(image=img)
#    instance.thumbnail=f'media/thumbnail{document_thumbnail_converted[0]}'


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
        verbose_name_plural = "Admin Info"

    def save(self, *args, **kwargs):
        self.department = self.get_department_display()
        self.role = self.get_role_display()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lastname
