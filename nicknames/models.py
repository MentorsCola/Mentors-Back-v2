from django.db import models


class Nicknames(models.Model):
    id = models.IntegerField(primary_key=True)
    names = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'nicknames'
