"""
Aticle model for SuperZapato test
"""
from __future__ import unicode_literals
from django.db import models

class articles(models.Model):
    """Modelo clase de compras de bdpruebapython"""
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, blank=False)
    total_in_shelf = models.PositiveIntegerField(null=False, blank=False)
    total_in_vault = models.PositiveIntegerField(null=False, blank=False)
    store_id = models.ForeignKey('Store.stores', null=False, blank=False, default=None, db_column="id_store")

    class Meta:
        db_table = 'articles'

    def __unicode__(self):
        return self.name