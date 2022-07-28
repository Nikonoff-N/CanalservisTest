from django.db import models


class Order(models.Model):
    order = models.IntegerField()
    dollar = models.FloatField()
    date = models.CharField(max_length=256)
    rub = models.FloatField()

    class Meta:
        managed = False
        db_table = 'order'