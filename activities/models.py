from django.db import models
from common.models import CommonModel


class Activity(CommonModel):
    name = models.CharField(max_length=180)
    address = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    # photo
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    start_day = models.DateField(null=True)
    close_day = models.DateField(null=True)
    temperature = models.IntegerField(null=True)
