from django.db import models
from settings.settings import setupConfigurations

setupConfigurations()

class TestModel(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)