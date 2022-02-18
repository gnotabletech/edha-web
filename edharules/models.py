from django.db import models


# Create your models here.
class EDHARule(models.Model):
    rule_section_num = models.IntegerField(default=1)
    rule_section_title = models.CharField(max_length=255)
    rule_subsection_num = models.IntegerField(default=1)
    rule_subsection_title = models.CharField(max_length=255)
    rule_details = models.TextField()

    class Meta:
        ordering = ['rule_section_num', 'rule_subsection_num']

    def __str__(self):
        return self.rule_subsection_title
