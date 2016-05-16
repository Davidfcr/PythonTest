"""
Store model for SuperZapato test
"""
from __future__ import unicode_literals
from django.db import models

class stores(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    address = models.CharField(max_length=40, null=False, blank=False)

    class Meta:
        db_table = 'stores'

    def __unicode__(self):
        return self.name