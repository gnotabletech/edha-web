from django.db import models


# Create your models here.
class EDHARule(models.Model):
    rule_section_num = models.IntegerField
    rule_section_title = models.CharField(max_length=255)
    rule_subsection_num = models.CharField(max_length=2)
    rule_subsection_title = models.CharField(max_length=255)
    rule_details = models.CharField(max_length=3000)

    def __str__(self):
        return self.rule_subsection_title
