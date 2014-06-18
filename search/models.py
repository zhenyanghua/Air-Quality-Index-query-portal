# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class Hourlydata(models.Model):
    rowid = models.IntegerField(primary_key=True)
    locationid = models.IntegerField(blank=True, null=True)
    stationname = models.CharField(max_length=255, blank=True)
    chinesename = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    pm25 = models.CharField(max_length=10, blank=True)
    pm10 = models.CharField(max_length=10, blank=True)
    o3 = models.CharField(max_length=10, blank=True)
    no2 = models.CharField(max_length=10, blank=True)
    so2 = models.CharField(max_length=10, blank=True)
    co = models.CharField(max_length=10, blank=True)
    temperature = models.CharField(max_length=10, blank=True)
    dewpoint = models.CharField(max_length=10, blank=True)
    pressure = models.CharField(max_length=10, blank=True)
    humidity = models.CharField(max_length=10, blank=True)
    wind = models.CharField(max_length=10, blank=True)
    est_time = models.BigIntegerField(blank=True, null=True)
    unix_time = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hourlydata'

class Location(models.Model):
    locationid = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    stationname = models.CharField(max_length=255, blank=True)
    parentcity = models.CharField(max_length=255, blank=True)
    sourceurl = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'location'

class Url(models.Model):
    stationname = models.CharField(max_length=255, blank=True)
    cnname = models.CharField(max_length=255, blank=True)
    sourceurl = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'url'

